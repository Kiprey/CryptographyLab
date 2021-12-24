#include "RC4.h"

/* 
初始置换得到S盒
S为S盒，key是密钥
*/
void rc4Init(unsigned char *S, string key)
{
    unsigned long len = key.length();
    int i = 0, j = 0;
    char k[256] = {0};
    unsigned char temp = 0;
    for (i = 0; i < 256; i++)
    {
        S[i] = i;
        k[i] = key[i % len];
    }
    for (i = 0; i < 256; i++)
    {
        j = (j + S[i] + k[i]) % 256;
        temp = S[i];
        S[i] = S[j]; //交换s[i]和s[j]
        S[j] = temp;
    }
}

string rc4Crypt(unsigned char *s, string data)
{
    unsigned long len = data.length();
    int i = 0, j = 0, t = 0;
    unsigned long k = 0;
    unsigned char temp;
    string RC4_result = data; //加解密的结果
    for (k = 0; k < len; k++)
    {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        temp = s[i];
        s[i] = s[j]; //交换s[x]和s[y]
        s[j] = temp;
        t = (s[i] + s[j]) % 256;
        RC4_result[k] = data[k] ^ s[t];
    }
    return RC4_result;
}
