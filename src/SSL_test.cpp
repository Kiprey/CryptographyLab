#include "network.h"
#include <unistd.h>
#include <iostream>
#include <sys/socket.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <cassert>

#define SYS_ERR(x)  \
    do {            \
        perror(x);  \
        abort();    \
    } while(0)

#define OPENSSL_ASSERT(x)                   \
    do {                                    \
        if(!(x)) {                          \
            ERR_print_errors_fp(stderr);    \
            abort();                        \
        }                                   \
    } while(0)

// 默认 CA 证书存放位置
#define DEFAULT_CA_CER_PATH         "../../crt/ca.crt"
// 默认 Server 公钥证书和私钥存放位置
#define DEFAULT_SERVER_CER_PATH     "../../crt/server.crt"
#define DEFAULT_SERVER_KEY_PATH     "../../crt/server.key"
// 默认 Client 公钥证书和私钥存放位置
#define DEFAULT_CLIENT_CER_PATH     "../../crt/client.crt"
#define DEFAULT_CLIENT_KEY_PATH     "../../crt/client.key"

static void loadcheck_cer(SSL_CTX* ctx, const string& ca_crt_path, const string& crt_path, const string& key_path) {
    // 验证对端的公钥证书
    SSL_CTX_set_verify(ctx, SSL_VERIFY_PEER, NULL); 
    // 设置 CA 证书路径
    SSL_CTX_load_verify_locations(ctx, ca_crt_path.c_str(), NULL);

    OPENSSL_ASSERT(SSL_CTX_use_certificate_file(ctx, crt_path.c_str(), SSL_FILETYPE_PEM));
    OPENSSL_ASSERT(SSL_CTX_use_PrivateKey_file(ctx, key_path.c_str(), SSL_FILETYPE_PEM));

    if (!SSL_CTX_check_private_key(ctx)) {
        printf("Private key does not match the certificate public key\n");
        abort();
    }
}

static void SSL_print_cert(SSL* ssl) {
    char buf[2048];
    // 得到对端的证书并打印信息
    X509 *peer_cert = SSL_get_peer_certificate(ssl);
    if (peer_cert != NULL) {
        cout << "Peer's certificate:" << endl;

        const char *str = X509_NAME_oneline(X509_get_subject_name(peer_cert), buf, sizeof(buf));
        if(str) {
            assert(str == buf);
            cout << "\t" << "Subject: " << str << endl;
        }

        str = X509_NAME_oneline(X509_get_issuer_name(peer_cert), buf, sizeof(buf));
        if(str) {
            assert(str == buf);
            cout << "\t" << "Issuer: " << str << endl;
        }

        // 将获取到的证书释放
        X509_free(peer_cert);
    }
    else
        printf("Peer does not have certificate.\n");
}

static void client_routine(int client_fd, SSL *ssl) {
    char buf[2048];
    // 尝试通信
    SSL_set_fd(ssl, client_fd);
    OPENSSL_ASSERT(SSL_connect(ssl));
    // 输出 SSL 信息
    cout << "SSL connection using " << SSL_get_cipher(ssl) << endl;
    SSL_print_cert(ssl);
    
    string str;
    while(getline(cin, str)) {
        int wlen = SSL_write(ssl, str.c_str(), str.size());
        int rlen = SSL_read(ssl, buf, sizeof(buf));
        cout << "[SERVER] " << string(buf, rlen) << endl;
        assert(rlen == wlen);
    }
	SSL_shutdown(ssl);
}

static void server_routine(int client_fd, SSL *ssl) {
    char buf[2048];
    // 尝试通信
    SSL_set_fd(ssl, client_fd);
    OPENSSL_ASSERT(SSL_accept(ssl));
    // 输出 SSL 信息
    cout << "SSL connection using " << SSL_get_cipher(ssl) << endl;
    SSL_print_cert(ssl);
    
    while(true) {
        int rlen = SSL_read(ssl, buf, sizeof(buf));
        if(rlen <= 0)
            break;
        cout << "[CLIENT] " << string(buf, rlen) << endl;
        int wlen = SSL_write(ssl, buf, rlen);
        assert(rlen == wlen);
    }
}

static void get_cert_key_path(bool is_server, string& ca_path, string& cer_path, string& key_path) {
    char buf[1024];
    string path;

    string prefix = is_server ? "[SERVER] " : "[CLIENT] ";

    cout << prefix << "请输入 CA 证书路径(默认为“" << DEFAULT_CA_CER_PATH << "”)：";
    getline(cin, path);
    if(path.size() <= 1)
        path = DEFAULT_CA_CER_PATH;
    realpath(path.c_str(), buf);
    ca_path = buf;
    
    const char* defalt_cer_path = is_server ? DEFAULT_SERVER_CER_PATH : DEFAULT_CLIENT_CER_PATH;
    cout << prefix << "请输入 证书 文件路径(默认为“" << defalt_cer_path << "”)：";
    getline(cin, path);
    if(path.size() <= 1)
        path = defalt_cer_path;
    realpath(path.c_str(), buf);
    cer_path = buf;
    
    const char* defalt_key_path = is_server ? DEFAULT_SERVER_KEY_PATH : DEFAULT_CLIENT_KEY_PATH;
    cout << prefix << "请输入 私钥 文件路径(默认为“" << defalt_key_path << "”)：";
    getline(cin, path);
    if(path.size() <= 1)
        path = defalt_key_path;
    realpath(path.c_str(), buf);
    key_path = buf;

    cout << "[INFO] CA  证书路径：" << ca_path << endl;
    cout << "[INFO] 证书 文件路径：" << cer_path << endl;
    cout << "[INFO] 私钥 证书路径：" << key_path << endl;
}

int main(int argc, char *argv[])
{
    // 准备好打印调试信息
    SSL_load_error_strings();
    ERR_load_crypto_strings();
    // 初始化 SSL
    OpenSSL_add_ssl_algorithms();

    // 服务端 [usage] ./SSL_test <port>
    if (argc == 2)
    {
        string ca_path, cer_path, key_path;
        get_cert_key_path(true, ca_path, cer_path, key_path);
        // 指定 SSL 协议
        SSL_CTX *ctx = SSL_CTX_new(TLS_server_method());
        loadcheck_cer(ctx, ca_path, cer_path, key_path);
        SSL_CTX_set_cipher_list(ctx, SSL_TXT_ALL);
        SSL *ssl = SSL_new(ctx);

        cout << "[SERVER] 监听端口 " << argv[1] << " ..." << endl;
        int server_fd = socketBindAndListen(atoi(argv[1]));
        if (server_fd < 0)
            SYS_ERR("socketBindAndListen");
        handleSIGPIPE();
        int client_fd;
        if((client_fd = accept(server_fd, nullptr, nullptr)) < 0)
            SYS_ERR("accept");
        close(server_fd);
        cout << "[SERVER] 连接成功，等待 CLIENT 输入..." << endl;

        server_routine(client_fd, ssl);
        close(client_fd);

        SSL_free(ssl);
        SSL_CTX_free(ctx);
    }
    // 客户端 [usage] ./SSL_test <ip> <port>
    else if(argc == 3)
    {
        string ca_path, cer_path, key_path;
        get_cert_key_path(false, ca_path, cer_path, key_path);

        // 指定 SSL 协议
        SSL_CTX *ctx = SSL_CTX_new(TLS_client_method());
        loadcheck_cer(ctx, ca_path, cer_path, key_path);
        SSL *ssl = SSL_new(ctx);

        cout << "[CLIENT] 尝试连接 " << argv[1] << ":" << argv[2] << " ..." << endl;
        int client_fd = connect2Server(argv[1], atoi(argv[2]));
        if(client_fd < 0)
            SYS_ERR("connect2Server");
        cout << "[CLIENT] 连接成功，等待用户输入..." << endl;

        client_routine(client_fd, ssl);
        close(client_fd);

        SSL_free(ssl);
        SSL_CTX_free(ctx);
    }
    else {
        cout << "服务端 [usage] " << argv[0] << " <port>" << endl;
        cout << "客户端 [usage] " << argv[0] << " <ip> <port>" << endl;
    }

    return 0;
}