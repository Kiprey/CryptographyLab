## RSA加解密算法设计说明

### 加解密概述

明文：任意长度的字符串

密文：由5位一组的十进制数字组成的字符串

密钥：公钥(e,n)，私钥(d,n)。加密时自动生成，解密时用户输入。

#### RSA体制的组成部分

- **密钥生成**

- **加密**

- **解密**

#### RSA.h

```c
#pragma once
#include <string>
#include <iostream>
using namespace std;
//公钥(e,n)，私钥(d,n) 规定模数不超过16位，即最多为5位十进制
struct key
{
    int e;
    int d;
    int n;
};
key ProduceKey();                       //产生密钥
string publicEncrypt(string s, key k);  //RSA公钥加密,生成密文：5位一组的十进制数字
string privateDecrypt(string s, key k); //RSA私钥解密,生成明文：字符串
string privateEncrypt(string s, key k); //RSA私钥加密,作签名，生成密文：5位一组的十进制数字
string publicDecrypt(string s, key k);  //RSA公钥解密,作验证，生成明文：字符串
```

### 密钥生成

- 首先选取两个大素数*p*和*q*，计算*n* = *pq*；

- 随机选取加密密钥*e*，使*e*和(*p* - 1)(*q* - 1)互素；

- 用扩展欧几里德算法计算解密密钥*d*，以满足：

- $ ed = 1mod(p - 1)(q - 1) $，即$ d = e-1mod(p- 1)(q - 1)$

- 公开钥为(*e*, *n*)，秘密钥为(*d*, *n*)。

#### 函数代码

```c
//产生密钥
key ProduceKey()
{
    key k;
    g_p = RandomlyGeneratePrime(3, 65536 / 128, 1);  
    g_q = RandomlyGeneratePrime(3, 65536 / g_p, 1); //使k.n=g_p*g_q不超过2^16
    k.n = g_p * g_q;
    unsigned int t = (g_p - 1) * (g_q - 1);
    k.e = RandomlyGeneratePrime(2, t, t); //产生2到t-1的一个素数，且与t互质
    k.d = CalculateD(k.e, t);
    return k;
}
```

#### 产生素数函数

```c
//产生a到b-1的素数,且与t互质
unsigned int RandomlyGeneratePrime(unsigned int a, unsigned int b, unsigned int t)
{
    unsigned int e = 0;
    srand((unsigned int)time(0)); //设置随机数种子
    e = a + rand() % (b - a - 1); //产生随机数e，从e开始找素数作为我们随机生成的素数
    do
    {
        if (e >= b) //若该素数大于b-1，重新生成一个随机数
        {
            e = a + rand() % (b - a - 1);
        }
        if (JudgePrimeNum(e) && RelativePrime(e, t)) //判断e是否为素数,且与t互质
        {
            break;
        }
    } while (e++);
    cout << e << endl;
    return e;
}
```

### 求模函数

```c
//通过(a*a)%n =((a%n)*a)%n求(a^b)%n
unsigned int PowerModule(int a, int b, int n)
{
    unsigned int result = 1;
    while (b--)
    {
        result = (result * a) % n;
    }
    return result;
}
```

### 公钥解密，私钥解密

#### 公钥加密

- 数学变换：$C=M^emodn$
  - C：明文
  - M：密文
  - (e,n)：公钥

```c
//RSA公钥加密,生成密文：5位一组的十进制数字
string publicEncrypt(string s, key k)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i++)
    {
        int temp = PowerModule(s[i], k.e, k.n); //字符串中的每个字符对应一个5位数字
        int dividend = 10000;
        while (dividend) //将5位数字转化为字符加入结果
        {
            result += (temp / dividend + '0');
            temp %= dividend;
            dividend /= 10;
        }
    }
    return result;
}
```

#### 私钥解密

- 数学变换：$M=C^dmodn$
  - C：明文
  - M：密文
  - (d,n)：私钥

```c
//RSA私钥解密,生成明文：字符串
string privateDecrypt(string s, key k)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i += 5)
    {
        string single = s.substr(i, 5);
        unsigned int c = 0;
        int factor = 10000;
        for (int j = 0; j < 5; j++)
        {
            c += factor * (single[j] - '0');
            factor /= 10;
        }
        int temp = PowerModule(c, k.d, k.n);
        result += (char)temp;
    }
    return result;
}
```

### 私钥加密，公钥解密

- 做签名和验证

#### 私钥加密

- 数学变换：$C=M^dmodn$
  - C：明文
  - M：密文
  - (d,n)：私钥

```c
// RSA私钥加密,作签名，生成密文：5位一组的十进制数字
string privateEncrypt(string s, key k)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i++)
    {
        int temp = PowerModule(s[i], k.d, k.n); //字符串中的每个字符对应一个5位数字
        int dividend = 10000;
        while (dividend) //将5位数字转化为字符加入结果
        {
            result += (temp / dividend + '0');
            temp %= dividend;
            dividend /= 10;
        }
    }
    return result;
}
```

#### 公钥解密

数学变换：$C=M^emodn$

- C：明文
- M：密文
- (e,n)：公钥e

```c
// RSA公钥解密,作验证，生成明文：字符串
string publicDecrypt(string s, key k)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i += 5)
    {
        string single = s.substr(i, 5); //5位数字对应一个字符
        unsigned int c = 0;
        int factor = 10000;
        for (int j = 0; j < 5; j++)
        {
            c += factor * (single[j] - '0'); //将5位数字的字符串转化位int型
            factor /= 10;
        }
        int temp = PowerModule(c, k.e, k.n);
        result += (char)temp;
    }
    return result;
}
```

