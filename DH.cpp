#include <cstring>
#include <iostream>
#include <cassert>
#include <openssl/md5.h>
#include <openssl/rc4.h>
#include <openssl/rsa.h>
#include <openssl/dh.h>
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
string rc4_encrypt(const string &data, const string& pass)
{
    RC4_KEY key;
    RC4_set_key(&key, pass.length(), (u_char *)pass.c_str()); //设置密钥
    char buf[data.size()];
    RC4(&key, data.size(), (u_char *)data.c_str(), (u_char*)buf); //加密明文
    return string(buf, data.size());
}

//RC4解密
string rc4_decrypt(const string &outdata, const string& pass)
{
    // rc4 使用相同密钥即可解密
    return rc4_encrypt(outdata, pass);
}

static string get_msg_digest(const string& data) {
    return base64Encode(md5_encode(data), false);
}

Auth_DH::Auth_DH(int fd)
    : _fd(fd), _shared_key(){};
Auth_DH::~Auth_DH() {}

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
    OPENSSL_ASSERT(ret);

    // 指定 RSA 密钥长度, callback 为空
    RSA *rsa_key = RSA_new();
    ret = RSA_generate_key_ex(rsa_key, 2048, e, NULL);
    OPENSSL_ASSERT(ret);
    BN_free(e);

    // 获取序列化后的公钥
    BIO *pub = BIO_new(BIO_s_mem());
    PEM_write_bio_RSAPublicKey(pub, rsa_key);
    // 获取长度并将密钥对读取到字符串
    size_t pub_len = BIO_pending(pub);
    ret = BIO_read(pub, buf, pub_len);
    OPENSSL_ASSERT(ret);
    BIO_free_all(pub);

    // 1. 发送公钥
    string pub_msg(buf, pub_len);
    cout << "[INFO] 发送的服务器公钥：" << get_msg_digest(pub_msg) << endl;
    send_msg(_fd, pub_msg, RSA_PUB_MSG_START_FLAG, RSA_PUB_MSG_END_FLAG);
    // 2. 接收被发送方加密后的第一个数 g^ra mod p
    string msg = recv_msg(_fd, NUM1_START_FLAG, NUM1_END_FLAG);
    // 解密
    ret = RSA_private_decrypt(msg.size(), (u_char *)msg.c_str(), (u_char *)buf, rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_ASSERT(ret);
    cout << "[INFO] 接收的 DH 公钥：" << get_msg_digest(string(buf, ret)) << endl;
    BIGNUM *g_ra_bn = BN_new();
    const BIGNUM* ret_bn = BN_bin2bn((u_char*)buf, ret, g_ra_bn);
    OPENSSL_ASSERT(ret_bn == g_ra_bn);

    // 3. 生成 rb, 并发送 g^rb mod p
    // 首先生成公共 G 和 P
    /// NOTE: 注意公钥长度不能大于 RSA 密钥长度
    DH* privkey = DH_get_1024_160();
    // 生成私钥
    ret = DH_generate_key(privkey);
    OPENSSL_ASSERT(ret);

    // 将 公钥 序列化
    const BIGNUM* g_rb_bn = DH_get0_pub_key(privkey);

    ret = BN_bn2bin(g_rb_bn, (u_char*)buf);
    OPENSSL_ASSERT(ret);
    string g_rb_str(buf, ret);
    cout << "[INFO] 发送的 DH 公钥：" << get_msg_digest(g_rb_str) << endl;
    // 用私钥加密
    assert(g_rb_str.size() <= RSA_size(rsa_key) - 11);
    ret = RSA_private_encrypt(g_rb_str.size(), (u_char *)g_rb_str.c_str(), (u_char *)buf, rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_ASSERT(ret >= 0);

    // 将加密内容发送
    string rb_msg(buf, ret);
    send_msg(_fd, rb_msg, NUM2_START_FLAG, NUM2_END_FLAG);

    // 4. 构建 g^(ra * rb) mod p
    char key[DH_size(privkey)];
    DH_compute_key((u_char*)key, g_ra_bn, privkey);
    _shared_key = string(key, DH_size(privkey));

    // 清除密钥
    RSA_free(rsa_key);
    BN_free(g_ra_bn);
    DH_free(privkey);

    // 输出共享密钥
    cout << "[INFO] 共享密钥：" << get_msg_digest(_shared_key) << endl;
    
    return true;
}

bool Auth_DH::client_exchange_key()
{
    ssize_t ret;
    char buf[2048];
    // 1. 接收服务器公钥
    string msg = recv_msg(_fd, RSA_PUB_MSG_START_FLAG, RSA_PUB_MSG_END_FLAG);
    cout << "[INFO] 接收的服务器公钥：" << get_msg_digest(msg) << endl;

    BIO *bio = BIO_new(BIO_s_mem());
    ret = BIO_puts(bio, msg.c_str());
    OPENSSL_ASSERT(ret);
    RSA *pub_rsa_key = PEM_read_bio_RSAPublicKey(bio, nullptr, nullptr, nullptr);
    OPENSSL_ASSERT(pub_rsa_key);
    BIO_free_all(bio);

    // 2. 生成 g^ra
    // 首先生成 G 和 P
    DH* privkey = DH_get_1024_160();
    // 之后生成私钥 ra
    ret = DH_generate_key(privkey);
    OPENSSL_ASSERT(ret);
    // 生成 G^ra mod p
    const BIGNUM *DH_RA_bn = DH_get0_pub_key(privkey);

    // 将 DH_RA_bn 序列化
    ret = BN_bn2bin(DH_RA_bn, (u_char*)buf);
    OPENSSL_ASSERT(ret);
    string g_ra_str(buf, ret);
    cout << "[INFO] 发送的 DH 公钥：" << get_msg_digest(g_ra_str) << endl;
    // 用公钥加密
    assert(g_ra_str.size() <= RSA_size(pub_rsa_key) - 11);
    ret = RSA_public_encrypt(g_ra_str.size(), (u_char *)g_ra_str.c_str(), (u_char *)buf, pub_rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_ASSERT(ret >= 0);

    // 将加密内容发送
    string ra_msg(buf, ret);
    send_msg(_fd, ra_msg, NUM1_START_FLAG, NUM1_END_FLAG);

    // 3. 接收 g^rb mod p
    msg = recv_msg(_fd, NUM2_START_FLAG, NUM2_END_FLAG);
    ret = RSA_public_decrypt(msg.size(), (u_char *)msg.c_str(), (u_char *)buf, pub_rsa_key, RSA_PKCS1_PADDING);
    OPENSSL_ASSERT(ret);
    cout << "[INFO] 接收的 DH 公钥：" << get_msg_digest(string(buf, ret)) << endl;
    BIGNUM *g_rb_bn = BN_new();
    const BIGNUM* ret_bn = BN_bin2bn((u_char*)buf, ret, g_rb_bn);
    OPENSSL_ASSERT(ret_bn == g_rb_bn);

    // 4. 构建 g^(ra * rb) mod p
    char key[DH_size(privkey)];
    DH_compute_key((u_char*)key, g_rb_bn, privkey);
    _shared_key = string(key, DH_size(privkey));

    // 清除公钥
    RSA_free(pub_rsa_key);
    BN_free(g_rb_bn);
    DH_free(privkey);

    // 输出共享密钥
    cout << "[INFO] 共享密钥：" << get_msg_digest(_shared_key) << endl;

    return true;
}

void Auth_DH::send(string msg)
{
    assert(!msg.empty());
    /**
     * 发送方 A 构建子串 E_k(m) || H(m || key)
     * 可以验证信息确实来源于一个保存正确 key 的终端
     */
    string H_mkey = md5_encode(msg + _shared_key);
    cout << "[MSG] send md5(msg || key)：" << base64Encode(H_mkey, false) << endl;
    assert(H_mkey.size() == 16);
    string e_km = rc4_encrypt(msg, _shared_key);
    send_msg(_fd, e_km + H_mkey, COM_START_FLAG, COM_END_FLAG);
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

    string msg_content = rc4_decrypt(e_km, _shared_key);
    string curr_H_mkey = md5_encode(msg_content + _shared_key);
    cout << "[MSG] recv md5(msg || key)：" << base64Encode(H_mkey, false) << endl;

    // 验证
    if(curr_H_mkey != H_mkey) {
        cout << "[MSG] ERR! md5 mismatch. calc md5(msg || key)：" << base64Encode(curr_H_mkey, false) << endl;
        return "";
    }
    return msg_content;
}
