#include <cstring>
#include <iostream>
#include <cassert>
#include <openssl/md5.h>
#include <openssl/rc4.h>
#include <openssl/rsa.h>
#include <openssl/buffer.h>
#include <openssl/pem.h>
#include "DH.h"
#include "network.h"

using namespace std;

string base64Encode(const string &buffer, bool newLine)
{

    BIO *b64 = BIO_new(BIO_f_base64());
    if (!newLine)
    {
        BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    }
    BIO *bmem = BIO_new(BIO_s_mem());
    b64 = BIO_push(b64, bmem);
    BIO_write(b64, buffer.c_str(), buffer.length());
    BIO_flush(b64);
    BUF_MEM *bptr;
    BIO_get_mem_ptr(b64, &bptr);
    BIO_set_close(b64, BIO_NOCLOSE);

    string buff(bptr->data, bptr->length);
    BIO_free_all(b64);

    return buff;
}

string base64Decode(const string &input, bool newLine)
{
    BIO *b64 = BIO_new(BIO_f_base64());
    if (!newLine)
    {
        BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    }
    BIO *bmem = BIO_new_mem_buf(input.c_str(), input.size());
    bmem = BIO_push(b64, bmem);

    char buffer[input.length()];
    BIO_read(bmem, buffer, input.length());
    BIO_free_all(bmem);

    return string(buffer, input.length());
}

string md5_encode(const string &input)
{
    char MD5result[MD5_DIGEST_LENGTH] = {0};
    MD5((u_char *)input.c_str(), input.size(), (u_char *)MD5result);
    return string(MD5result, sizeof(MD5result));
}

//RC4加密
string rc4_encrypt(const string &data, const char *pass)
{
    RC4_KEY key;
    int length = strlen(pass);
    RC4_set_key(&key, length, (u_char *)pass); //设置密钥
    char buf[data.size()];
    RC4(&key, data.size(), (u_char *)data.c_str(), (u_char*)buf); //加密明文
    return string(buf, data.size());
}

//RC4解密
string rc4_decrypt(const string &outdata, const char *pass)
{
    RC4_KEY key;
    int length = strlen(pass);
    RC4_set_key(&key, length, (u_char *)pass);                    //设置密钥
    char buf[outdata.size()];
    RC4(&key, outdata.size(), (u_char *)outdata.c_str(), (u_char*)buf); //解密密文
    return string(buf, outdata.size());
}

Auth_DH::Auth_DH(int fd)
    : _fd(fd), _shared_key(BN_new()){};
Auth_DH::~Auth_DH()
{
    BN_free(_shared_key);
}

void Auth_DH::_generate_G_and_P(BIGNUM **G_bn, BIGNUM **P_bn, BN_CTX *ctx)
{
    // 生成 P
    *P_bn = BN_new();
    BIGNUM *P_base_bn = BN_new();
    ssize_t ret = BN_set_word(P_base_bn, P_base);
    assert(ret);
    BIGNUM *P_exp_bn = BN_new();
    ret = BN_set_word(P_exp_bn, P_exp);
    assert(ret);
    ret = BN_exp(*P_bn, P_base_bn, P_exp_bn, ctx);
    assert(ret);
    BN_free(P_base_bn);
    BN_free(P_exp_bn);

    // 生成 G
    *G_bn = BN_new();
    ret = BN_set_word(*G_bn, G);
    assert(ret);
}

bool Auth_DH::server_exchange_key()
{
    // 一个临时缓冲区
    char buf[2048];
    // 一个用于接收函数返回值的变量
    ssize_t ret;

    /**
     * 1. 双方创建随机数 ra 和 rb
     * 2. 服务端创建公钥私钥，并发送公钥给客户端（这一步省略了客户端去验证公钥证书有效性）
     * 3. 客户端使用该公钥发送加密 g^ra 并发送给服务端
     * 4. 服务端使用私钥加密并用公钥解开
     */
    // 创建 RSA 密钥（因为只有服务端才会准备 RSA 密钥）
    // 指定 e 为 0x10001
    BIGNUM *e = BN_new();
    ret = BN_set_word(e, RSA_F4);
    assert(ret);

    // 指定 RSA 密钥长度, callback 为空
    RSA *rsa_key = RSA_new();
    ret = RSA_generate_key_ex(rsa_key, RSA_BITS_NUM, e, NULL);
    assert(ret);
    BN_free(e);

    // 获取序列化后的公钥
    BIO *pub = BIO_new(BIO_s_mem());
    PEM_write_bio_RSAPublicKey(pub, rsa_key);

    // 获取长度并将密钥对读取到字符串
    size_t pub_len = BIO_pending(pub);
    ret = BIO_read(pub, buf, pub_len);
    assert(ret);
    BIO_free_all(pub);

    // 1. 发送公钥
    string pub_msg(buf, pub_len);
    cout << "[INFO] 发送的服务器公钥：" << pub_msg << endl;
    send_msg(_fd, pub_msg, RSA_PUB_MSG_START_FLAG, RSA_PUB_MSG_END_FLAG);
    // 2. 接收被发送方加密后的第一个数 g^ra mod p
    string msg = recv_msg(_fd, NUM1_START_FLAG, NUM1_END_FLAG);
    // 解密
    ret = RSA_private_decrypt(msg.size(), (u_char *)msg.c_str(), (u_char *)buf, rsa_key, RSA_PKCS1_PADDING);
    assert(ret);

    BIGNUM *g_ra_bn = BN_new();
    ret = BN_hex2bn(&g_ra_bn, buf);
    assert(ret > 0);

    // 3. 生成 rb, 并发送 g^rb mod p
    // 首先生成 rb
    BIGNUM *rb = BN_new();
    ret = BN_rand(rb, SINGLE_KEY_LEN, -1, 1); //生成指定bits的随机数
    assert(ret);
    // 之后生成 G 和 P
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *G_bn, *P_bn;
    _generate_G_and_P(&G_bn, &P_bn, ctx);
    // 生成 G^rb mod p
    BIGNUM *DH_RB_bn = BN_new();
    ret = BN_mod_exp(DH_RB_bn, G_bn, rb, P_bn, ctx);
    assert(ret);

    // 将 DH_RB_bn 序列化
    char *rb_hex = BN_bn2hex(DH_RB_bn);
    cout << "[INFO] 发送的 G^rb mod P：" << rb_hex << endl;
    BN_free(DH_RB_bn);
    // 用私钥加密
    assert(strlen(rb_hex) <= RSA_size(rsa_key));
    ret = RSA_private_encrypt(RSA_size(rsa_key) - 11, (u_char *)rb_hex, (u_char *)buf, rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_free(rb_hex);
    assert(ret >= 0);

    // 将加密内容发送
    string rb_msg(buf, ret);
    send_msg(_fd, rb_msg, NUM2_START_FLAG, NUM2_END_FLAG);

    // 4. 构建 g^(ra * rb) mod p
    ret = BN_mod_exp(_shared_key, g_ra_bn, rb, P_bn, ctx);
    assert(ret);

    // 清除 RSA 密钥
    RSA_free(rsa_key);

    // 输出共享密钥
    char *rarb_hex = BN_bn2hex(_shared_key);
    cout << "[INFO] 共享密钥 G^(rarb) mod P：" << rarb_hex << endl;
    OPENSSL_free(rarb_hex);
    
    return true;
}

bool Auth_DH::client_exchange_key()
{
    ssize_t ret;
    char buf[2048];
    // 1. 接收服务器公钥
    string msg = recv_msg(_fd, RSA_PUB_MSG_START_FLAG, RSA_PUB_MSG_END_FLAG);
    cout << "[INFO] 接收的服务器公钥：" << msg << endl;

    BIO *bio = BIO_new(BIO_s_mem());
    ret = BIO_puts(bio, msg.c_str());
    assert(ret);
    RSA *pub_rsa_key = PEM_read_bio_RSAPublicKey(bio, nullptr, nullptr, nullptr);
    assert(pub_rsa_key);
    BIO_free_all(bio);

    // 2. 生成 g^ra
    // 首先生成 ra
    BIGNUM *ra = BN_new();
    ret = BN_rand(ra, SINGLE_KEY_LEN, -1, 1); //生成指定bits的随机数
    assert(ret);
    // 之后生成 G 和 P
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *G_bn, *P_bn;
    _generate_G_and_P(&G_bn, &P_bn, ctx);
    // 生成 G^ra mod p
    BIGNUM *DH_RA_bn = BN_new();
    ret = BN_mod_exp(DH_RA_bn, G_bn, ra, P_bn, ctx);
    assert(ret);

    // 将 DH_RA_bn 序列化
    char *ra_hex = BN_bn2hex(DH_RA_bn);
    cout << "[INFO] 发送的 G^ra mod P：" << ra_hex << endl;
    BN_free(DH_RA_bn);
    // 用公钥加密
    assert(strlen(ra_hex) <= RSA_size(pub_rsa_key));
    ret = RSA_public_encrypt(RSA_size(pub_rsa_key) - 11, (u_char *)ra_hex, (u_char *)buf, pub_rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_free(ra_hex);
    assert(ret >= 0);

    // 将加密内容发送
    string ra_msg(buf, ret);
    send_msg(_fd, ra_msg, NUM1_START_FLAG, NUM1_END_FLAG);

    // 3. 接收 g^rb mod p
    msg = recv_msg(_fd, NUM1_START_FLAG, NUM1_END_FLAG);
    ret = RSA_public_decrypt(msg.size(), (u_char *)msg.c_str(), (u_char *)buf, pub_rsa_key, RSA_PKCS1_PADDING);
    assert(ret);
    BIGNUM *g_rb_bn = BN_new();
    ret = BN_hex2bn(&g_rb_bn, msg.c_str());
    assert(ret > 0);

    // 4. 构建 g^(ra * rb) mod p
    ret = BN_mod_exp(_shared_key, g_rb_bn, ra, P_bn, ctx);
    assert(ret);

    // 清除公钥
    BN_free(ra);
    RSA_free(pub_rsa_key);
    BN_free(G_bn);
    BN_free(P_bn);
    BN_CTX_free(ctx);

    // 输出共享密钥
    char *rarb_hex = BN_bn2hex(_shared_key);
    cout << "[INFO] 共享密钥 G^(rarb) mod P：" << rarb_hex << endl;
    OPENSSL_free(rarb_hex);

    return true;
}

void Auth_DH::send(string msg)
{
    assert(!msg.empty());
    /**
     * 发送方 A 构建子串 E_k(m) || H(m || key)
     * 可以验证信息确实来源于一个保存正确 key 的终端
     */
    char *key_hex = BN_bn2hex(_shared_key);
    string H_mkey = md5_encode(msg + key_hex);
    assert(H_mkey.size() == 16);
    string e_km = rc4_encrypt(msg, key_hex);
    send_msg(_fd, e_km + H_mkey, COM_START_FLAG, COM_END_FLAG);
    OPENSSL_free(key_hex);
}

string Auth_DH::recv(void)
{
    /**
     * 接收方验证 消息完整性和消息来源
     */
    string msg = recv_msg(_fd, COM_START_FLAG, COM_END_FLAG);
    assert(msg.size() >= 16);
    string H_mkey = msg.substr(msg.size() - 16);
    string e_km = msg.substr(0, msg.size() - 16);

    char *key_hex = BN_bn2hex(_shared_key);
    string msg_content = rc4_decrypt(e_km, key_hex);
    string curr_H_mkey = md5_encode(msg_content + key_hex);
    OPENSSL_free(key_hex);

    // 验证
    return curr_H_mkey == H_mkey ? msg_content : "";
}
