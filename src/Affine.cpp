#include "Affine.h"
#include <algorithm>
#include <iostream>
#include <cctype>

static int gcd(int s, int t) //求最小公因数
{
    if (t == 0)
    {
        return s;
    }
    return gcd(t, s % t);
}

static int exgcd(int a, int b, int &x, int &y) //扩展欧几里得
{
    if (b == 0)
    {
        x = 1;
        y = 0;
        return a;
    }
    int ans = exgcd(b, a % b, x, y);
    int temp = x;
    x = y;
    y = temp - a / b * y;
    return ans;
}

static int calInverse(int a, int m) //计算逆元
{
    int x, y;
    int gcd = exgcd(a, m, x, y);
    if (1 % gcd != 0)
        return -1;
    x *= 1 / gcd;
    m = abs(m);
    int ans = x % m;
    if (ans <= 0)
        ans += m;
    return ans;
}

bool affineEncryption(int key1, int key2, string plaintext, string &ciphertext)
{
    //判断密钥是否合法
    if (gcd(26, key1) == 1 && key1 >= 0 && key2 >= 0 && key1 < 26)
    {
        key2 = key2 % 26;
        ciphertext = ""; //清空密文
        for (int i = 0; i < plaintext.length(); i++)
        {
            if (isalpha(plaintext[i])) //处理字母，其它字符会被忽略
            {
                if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') //将大写字母转换为小写字母
                    plaintext[i] = plaintext[i] + 32;
                int code = plaintext[i] - 'a';    //字符变数字
                code = (key1 * code + key2) % 26; //加密 c=key1*m+key2 (mod 26)
                char temp = code + 'a';           //数字变字符
                ciphertext = ciphertext + temp;   //得到密文
            }
        }
        return 1;
    }
    //密钥不合法返回0
    else
        return 0;
}

bool affineDecryption(int key1, int key2, string ciphertext, string &clear_text)
{
    if (gcd(26, key1) == 1 && key1 >= 0 && key2 >= 0 && key1 < 26)
    {
        key2 = key2 % 26;
        clear_text = ""; //清空明文
        for (int i = 0; i < ciphertext.length(); i++)
        {
            int code = ciphertext[i] - 'a'; //字符变数字
            //解密 m=(c-key2+26)*key1^(-1) mod 26
            code = ((code - key2 + 26) * calInverse(key1, 26)) % 26;
            char temp = code + 'a';         //数字变字符
            clear_text = clear_text + temp; //得到明文
        }
        return 1; //返回解密的明文
    }
    else
        return 0;
}