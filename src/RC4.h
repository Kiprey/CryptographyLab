#ifndef RC4_H
#define RC4_H

#include <string>
using namespace std;

/* 
初始置换得到S盒
S为S盒，key是密钥
*/
void rc4Init(unsigned char *s, string key);

/*
RC4加解密函数
S为初始置换后的S盒，data是待加密的密文或者待解密的明文
*/
string rc4Crypt(unsigned char*S, string data);

#endif