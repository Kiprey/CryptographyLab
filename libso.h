#ifndef LIBSO_H
#define LIBSO_H

#include "DES.h"
#include "DH.h"
#include "network.h"
#include "Affine.h"
#include "RC4.h"
#include "LFSR.h"
#include "RSA.h"

extern "C" {
    // DES 协议相关 ------------------
    
    /**
     * @brief 设置 DES 密钥
     * @param k 密钥字符串参数
     */ 
    void DES_generateKeys(const char* k);

    /**
     * @brief DES 加密
     * @param s 明文字符串
     * @return 加密后的密文，无需释放其内存
     */ 
    const char* DES_encrypt(const char* s);

    /**
     * @brief DES 解密
     * @param s 密文字符串
     * @return 解密后的明文，无需释放其内存
     */ 
    const char* DES_decrypt(const char *s);

    // DH 协议相关 ------------------

    /**
     * @brief 创建 DH 协议对象
     * @param fd 套接字的文件描述符
     * @return 新创建的 DH 对象指针
     */ 
    void* Auth_DH_new(int fd);

    /**
     * @brief 释放 DH 协议对象
     * @param ptr DH 对象的指针
     */ 
    void Auth_DH_free(void* ptr);

    /**
     * @brief 服务端执行 DH 密钥协商
     * @param ptr DH 对象的指针
     * @return 是否协商成功，true 表示成功
     */ 
    bool Auth_DH_server_exch_key(void* ptr);
    
    /**
     * @brief 客户端执行 DH 密钥协商
     * @param ptr DH 对象的指针
     * @return 是否协商成功，true 表示成功
     */ 
    bool Auth_DH_client_exch_key(void* ptr);

    /**
     * @brief 数据发送
     * @param ptr DH 对象的指针
     * @param msg 等待发送的数据
     * @return 数据发送是否成功，true 表示成功
     */ 
    bool Auth_DH_send(void* ptr, const char* msg);

    /**
     * @brief 数据接收
     * @param ptr DH 对象的指针
     * @return 接收到的数据，NULL 表示接收失败。该指针无需释放
     */ 
    const char* Auth_DH_recv(void* ptr);

    // SSL 相关 ------------------

    /**
     * @brief 输出证书信息
     * @param ptr SSL* 类型的对象
     * @return 指向输出信息的指针。该指针无需释放
     * @note 注意，只能在 SSL_my_accept/ SSL_my_connect 成功执行后使用
     */ 
    const char* SSL_print_cert(void* ptr); 

    /**
     * @brief SSL 初始化
     * @param ret_ssl 存放新生成的 SSL* 指针的地址空间
     * @param ret_ctx 存放新生成的 SSL_CTX* 指针的地址空间
     * @param is_server 当前是否是服务端，true 表示是服务端进行 SSL 初始化
     * @param ca_cert_path CA 公钥证书路径
     * @param cer_path 自己证书的路径
     * @param key_path 自己私钥的路径
     * @return 是否成功执行操作， false 表示执行失败
     */ 
    bool SSL_my_init(void**ret_ssl, void**ret_ctx, bool is_server, 
                  const char* ca_cert_path, const char* cer_path, const char* key_path);

    /**
     * @brief 释放 SSL 资源
     * @param ssl SSL* 类型的对象
     * @param ctx SSL_CTX* 类型的对象
     */ 
    void SSL_my_deinit(void*ssl, void* ctx);

    /**
     * @brief 向远程发起 SSL 连接请求
     * @param client_fd 套接字文件描述符
     * @param in_ssl SSL* 类型的对象
     * @return 是否成功执行操作， false 表示执行失败
     */ 
    bool SSL_my_connect(int client_fd, void *in_ssl);

    /**
     * @brief 接受远程发起的 SSL 连接请求
     * @param client_fd 套接字文件描述符
     * @param in_ssl SSL* 类型的对象
     * @return 是否成功执行操作， false 表示执行失败
     */ 
    bool SSL_my_accept(int client_fd, void *in_ssl);

    /**
     * @brief SSL 数据接收
     * @param ssl SSL* 类型的对象
     * @param buf 指向缓冲区的指针
     * @param len 待接收的长度
     * @return 接收成功的字节长度
     */ 
    int SSL_my_read(void* ssl, char*buf, int len);

    /**
     * @brief SSL 数据发送
     * @param ssl SSL* 类型的对象
     * @param buf 指向缓冲区的指针
     * @param len 待发送的长度
     * @return 发送成功的字节长度
     */ 
    int SSL_my_write(void* ssl, char*buf, int len);

    // 仿射加密相关 ------------------

    /**
     * @brief 仿射加密
     * @param key1 密钥1, 必须与26互素
     * @param key2 密钥2, 范围必须位于 [0, 26)
     * @param plain 待加密的明文
     * @param cipher 加密结果将输出至该指针所指向的内存空间
     */ 
    bool Affine_encrypt(int key1, int key2, const char* plain, char* cipher);

    /**
     * @brief 仿射解密
     * @param key1 密钥1, 必须与26互素
     * @param key2 密钥2, 范围必须位于 [0, 26)
     * @param cipher 待解密的密文
     * @param plain 解密结果将输出至该指针所指向的内存空间
     */ 
    bool Affine_decrypt(int key1, int key2, const char* cipher, char* plain);

    // RC4相关 ------------------

    /**
     * @brief RC4 密钥设置
     * @param s 一个指向存放S盒的内存指针，其所指向的空间至少为 256 字节
     * @param key 待设置的密钥
     */ 
    void RC4_set_key(unsigned char* s, const char* key);

    /**
     * @brief RC4 加密解密函数。加密与解密都使用同一个函数
     * @param s 一个指向存放S盒的内存指针，其所指向的空间至少为 256 字节
     * @param data 待加密/解密的数据
     * @return 解密/加密后的数据。该指针无需用户释放
     */ 
    const char* RC4_enc_dec(unsigned char* s, const char* data);

    // LFSR 相关 ------------------

    /**
     * @brief LFSR 密钥设置
     * @param c 一个指向存放四个线性反馈寄存器的内存指针，其所指向的空间至少为 4 字节
     * @param key 待设置的密钥
     */ 
    void LFSR_set_key(unsigned char* c, const char* key);

    /**
     * @brief LFSR 加密解密函数。加密与解密都使用同一个函数
     * @param c 一个指向存放四个线性反馈寄存器的内存指针，其所指向的空间至少为 4 字节
     * @param data 待加密/解密的数据
     * @return 解密/加密后的数据。该指针无需用户释放
     */ 
    const char* LFSR_enc_dec(unsigned char* c, const char* data);

    // RSA 相关 ------------------

    /**
     * @brief RSA 密钥生成
     * @param e 指向存放 e 的整形指针
     * @param d 指向存放 d 的整形指针
     * @param n 指向存放 n 的整形指针
     */ 
    void RSA_gen_key(int* e, int* d, int* n);

    /**
     * @brief RSA 公钥加密
     * @param data 明文
     * @param e 公钥之一
     * @param n 公钥之一
     * @return 加密后的结果
     */ 
    const char* RSA_pubkey_encrypt(const char* data, int e, int n);
    
    /**
     * @brief RSA 公钥解密
     * @param data 密文
     * @param d 公钥之一
     * @param n 公钥之一
     * @return 解密后的结果
     */
    const char* RSA_pubkey_decrypt(const char* data, int e, int n);

    /**
     * @brief RSA 私钥加密
     * @param data 明文
     * @param d 私钥之一
     * @param n 私钥之一
     * @return 加密后的结果
     */
    const char* RSA_privkey_encrypt(const char* data, int d, int n);

    /**
     * @brief RSA 私钥解密
     * @param data 密文
     * @param d 私钥之一
     * @param n 私钥之一
     * @return 解密后的结果
     */
    const char* RSA_privkey_decrypt(const char* data, int d, int n);
}

#endif