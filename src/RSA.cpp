#include <iostream>
#include <string>
#include <cmath>
#include <unistd.h>
#include <stdlib.h>
#include "time.h"
#include "RSA.h"
using namespace std;

static int g_p, g_q;
static bool JudgePrimeNum(unsigned int num);                          //判断num是否为素数
static unsigned int RandomlyGenerate(unsigned int a, unsigned int b); //产生a到b-1的随机数
static unsigned int gcd(unsigned int big, unsigned int small);        //求最大公因数
static bool RelativePrime(unsigned int big, unsigned int small);      //判断最大公因数是否是1，是1的话两个数就互质
static int CalculateD(unsigned int e, unsigned int model);            //求e*d = 1 mod (p-1)(q-1) 中的d
static unsigned int PowerModule(int a, int b, int n);

//判断num是否为素数
bool JudgePrimeNum(unsigned int num)
{
    unsigned int devider = 2;
    for (; devider < sqrt(num); devider++)
    {
        if (num % devider == 0)
            return false;
    }
    return true;
}

//求最大公因数
unsigned int gcd(unsigned int big, unsigned int small)
{
    int result;
    int tmp = 0;
    while (big % small)
    {

        tmp = small;
        small = big % small;
        big = tmp;
    }
    result = small;
    return result;
}

//判断最大公因数是否是1，是1的话两个数就互质
bool RelativePrime(unsigned int big, unsigned int small)
{
    if (big < small)
    {
        unsigned temp = small;
        small = big;
        big = temp;
    }
    unsigned int M = gcd(big, small);
    if (M == 1)
        return true;
    else
        return false;
}
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

//求e*d = 1 mod (p-1)(q-1) 中的d
int CalculateD(unsigned int e, unsigned int model)
{
    unsigned int d = 1;
    unsigned int reminder = d * e;
    while (reminder != 1)
    {
        d++;
        reminder = (reminder + e) % model;
    }
    return d;
}

//公钥(e,n)，私钥(d,n)
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

// RSA公钥加密,生成密文：5位一组的十进制数字
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

// RSA私钥解密,生成明文：字符串
string privateDecrypt(string s, key k)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i += 5)
    {
        string single = s.substr(i, 5); //5位数字对应一个字符
        unsigned int c = 0;
        int factor = 10000;
        for (int j = 0; j < 5; j++) //将5位数字的字符串转化位int型
        {
            c += factor * (single[j] - '0');
            factor /= 10;
        }
        int temp = PowerModule(c, k.d, k.n);
        result += (char)temp;
    }
    return result;
}

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