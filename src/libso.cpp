#include "libso.h"
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <cstring>

extern "C" {
    // DES 协议相关
    void DES_generateKeys(const char* k){
        string key = k;
        generateKeys(key);
    }
    const char* DES_encrypt(const char* s) {
        string msg = s;
        static string ret;
        ret = encrypt(msg);
        return ret.c_str();
    }
    const char* DES_decrypt(const char *s) {
        string msg = s;
        static string ret;
        ret = decrypt(msg);
        return ret.c_str();
    }

    // DH 协议相关
    void* Auth_DH_new(int fd) {
        Auth_DH* dh = new Auth_DH(fd);
        return dh;
    }
    void Auth_DH_free(void* ptr) {
        delete (Auth_DH*) ptr;
    }

    bool Auth_DH_server_exch_key(void* ptr) {
        return ((Auth_DH*)ptr)->server_exchange_key();
    }
    
    bool Auth_DH_client_exch_key(void* ptr) {
        return ((Auth_DH*)ptr)->client_exchange_key();
    }

    bool Auth_DH_send(void* ptr, const char* msg){
        string str = msg;
        return ((Auth_DH*)ptr)->send(str);
    }
    const char* Auth_DH_recv(void* ptr) {
        static string msg;
        if(!((Auth_DH*)ptr)->recv(msg))
            return NULL;
        return msg.c_str();
    }

    // SSL 相关
    const char* SSL_print_cert(void* ptr) {
        static string ret;
        SSL* ssl = (SSL*) ptr;
        char buf[2048];

        // 得到对端的证书并打印信息
        X509 *peer_cert = SSL_get_peer_certificate(ssl);
        if (peer_cert != NULL) {
            ret = "Peer's certificate:\n";

            const char *str = X509_NAME_oneline(X509_get_subject_name(peer_cert), buf, sizeof(buf));
            if(str) {
                ret += "\tSubject: ";
                ret += str;
                ret += "\n";
            }

            str = X509_NAME_oneline(X509_get_issuer_name(peer_cert), buf, sizeof(buf));
            if(str) {
                ret += "\tIssuer: ";
                ret += str;
                ret += "\n";
            }

            // 将获取到的证书释放
            X509_free(peer_cert);
        }
        else
            ret = "Peer does not have certificate.\n";
        return ret.c_str();
    }

    bool SSL_my_init(void**ret_ssl, void**ret_ctx, bool is_server, 
                  const char* ca_cert_path, const char* cer_path, const char* key_path) {
        // 准备好打印调试信息
        SSL_load_error_strings();
        ERR_load_crypto_strings();
        // 初始化 SSL
        OpenSSL_add_ssl_algorithms();

        const SSL_METHOD * meth = is_server ? TLS_server_method() : TLS_client_method();
        SSL_CTX *ctx = SSL_CTX_new(meth);

        // 验证对端的公钥证书
        SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL); 
        // 设置 CA 证书路径
        if(SSL_CTX_load_verify_locations(ctx, ca_cert_path, NULL) != 1)
            goto free_ctx;

        if(SSL_CTX_use_certificate_file(ctx, cer_path, SSL_FILETYPE_PEM) != 1) 
            goto free_ctx;
        if(SSL_CTX_use_PrivateKey_file(ctx, key_path, SSL_FILETYPE_PEM) != 1)
            goto free_ctx;

        if (SSL_CTX_check_private_key(ctx) != 1)
            goto free_ctx;

        if(SSL_CTX_set_cipher_list(ctx, SSL_TXT_ALL) != 1)
            goto free_ctx;

        *ret_ssl = SSL_new(ctx);
        *ret_ctx = ctx;
        return true;
    free_ctx:
        SSL_CTX_free(ctx);
        return false;
    }

    void SSL_my_deinit(void*ssl, void* ctx) {
	    SSL_shutdown((SSL*)ssl);
        SSL_free((SSL*)ssl);
        SSL_CTX_free((SSL_CTX*)ctx);
    }

    bool SSL_my_connect(int client_fd, void *in_ssl) {
        SSL* ssl = (SSL*)in_ssl;
        if(!SSL_set_fd(ssl, client_fd))
            return false;
        return SSL_connect(ssl) != 1;
    }

    bool SSL_my_accept(int client_fd, void *in_ssl) {
        SSL* ssl = (SSL*)in_ssl;
        if(!SSL_set_fd(ssl, client_fd))
            return false;
        return SSL_accept(ssl) != 1;
    }

    int SSL_my_read(void* ssl, char*buf, int len) {
        return SSL_read((SSL*)ssl, (void*)buf, len);
    }

    int SSL_my_write(void* ssl, char*buf, int len) {
        return SSL_write((SSL*)ssl, (void*)buf, len);
    }

    bool Affine_encrypt(int key1, int key2, const char* plain, char* cipher) {
        string ret;
        bool ret_b = affineEncryption(key1, key2, plain, ret);
        memcpy(cipher, ret.c_str(), ret.size());
        return ret_b;
    }

    bool Affine_decrypt(int key1, int key2, const char* cipher, char* plain) {
        string ret;
        bool ret_b = affineDecryption(key1, key2, cipher, ret);
        memcpy(plain, ret.c_str(), ret.size());
        return ret_b;
    }

    void RC4_set_key(unsigned char* s, const char* key) {
        rc4Init(s, key);
    }

    const char* RC4_enc_dec(unsigned char* s, const char* data) {
        static string ret;
        ret = rc4Crypt(s, data);
        return ret.c_str();
    }

    void LFSR_set_key(unsigned char* c, const char* key) {
        coefInit(c, key);
    }

    const char* LFSR_enc_dec(unsigned char* c, const char* data) {
        static string ret;
        ret = LFSR(data, c);
        return ret.c_str();
    }

    void RSA_gen_key(int* e, int* d, int* n) {
        key k = ProduceKey();
        *e = k.e;
        *d = k.d;
        *n = k.n;
    }

    const char* RSA_pubkey_encrypt(const char* data, int e, int n) {
        static string ret;
        ret = publicEncrypt(data, {e, -1, n});
        return ret.c_str();
    }

    const char* RSA_pubkey_decrypt(const char* data, int e, int n) {
        static string ret;
        ret = publicDecrypt(data, {e, -1, n});
        return ret.c_str();
    }

    const char* RSA_privkey_encrypt(const char* data, int d, int n) {
        static string ret;
        ret = privateEncrypt(data, {-1, d, n});
        return ret.c_str();
    }

    const char* RSA_privkey_decrypt(const char* data, int d, int n) {
        static string ret;
        ret = privateDecrypt(data, {-1, d, n});
        return ret.c_str();
    }
}