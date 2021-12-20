#ifndef DH_H
#define DH_H
#include <iostream>
#include <openssl/rsa.h>
#include <openssl/bn.h>
using namespace std;

/**
 * @brief base64 编码
 */ 
string base64Encode(const string& buffer, bool newLine);

/**
 * @brief base64 解码
 */ 

string base64Decode(const string& input, bool newLine);

/**
 *  @brief 计算 MD5 
 */
string md5_encode(const string& input);

/**
 *  @brief 使用 RC4 进行加密
 */
string rc4_encrypt(const string &data, const string& pass);

/**
 *  @brief 使用 RC4 进行解密
 */
string rc4_decrypt(const string &outdata, const string& pass);

/**
 * @brief 带有以下几种功能的 DH 通信协议
 *      1. 消息认证
 *      2. 消息完整性验证
 *      3. 加密保护
 */

// 网络通信交互用的信息头
#define RSA_PUB_MSG_START_FLAG   "[MSG_PUB_START]"
#define RSA_PUB_MSG_END_FLAG     "[MSG_PUB_END]"
#define NUM1_START_FLAG          "[MSG_NUM1_START]"
#define NUM1_END_FLAG            "[MSG_NUM1_END]"
#define NUM2_START_FLAG          "[MSG_NUM2_START]"
#define NUM2_END_FLAG            "[MSG_NUM2_END]"
#define COM_START_FLAG           "\x12[MSG_COM_START]\x21"
#define COM_END_FLAG             "\x12[MSG_COM_END]\x21"

class Auth_DH {
private:
    int _fd;
    string _shared_key;
public:
    // 创建 DH 协议通信
    Auth_DH(int fd);
    ~Auth_DH();
    // 密钥交换
    bool server_exchange_key();
    bool client_exchange_key();
    // 发送信息
    void send(string msg);
    // 接收信息
    string recv(void);
};

#endif