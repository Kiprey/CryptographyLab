#include <string>
#include <iostream>
#include <unistd.h>
#include "time.h"
#include "RSA.h"
using namespace std;

int g_p, g_q;
unsigned int g_d, g_e, g_n; //公钥(g_e,g_n)，私钥(g_d,g_n) 规定模数不超过16位，即最多为5位十进制

static bool JudgePrimeNum(unsigned int num);
static unsigned int RandomlyGenerate(unsigned int a, unsigned int b);
static unsigned int gcd(unsigned int big, unsigned int small);
static bool RelativePrime(unsigned int big, unsigned int small);
static int CalculateD(unsigned int e, unsigned int model);
static unsigned int PowerModule(int a, int b, int n);

//判断num是否为素数
bool JudgePrimeNum(unsigned int num)
{
    unsigned int devider = 2;
    for (; devider < num / 2; devider++)
    {
        if (num % devider == 0)
            return false;
    }
    return true;
}

//产生a到b-1的随机数
unsigned int RandomlyGenerate(unsigned int a, unsigned int b)
{
    unsigned int e = 0;
    srand((unsigned int)time(0)); //设置随机数种子
    e = a + rand() % (b - a - 1);
    return e; //随机数
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
    unsigned int M = gcd(big, small);
    if (M == 1)
        return true;
    else
        return false;
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
void ProduceKey()
{
    //g_p，g_q不超过256，g_n不会超过2^16
    g_p = RandomlyGenerate(3, 255);
    while (!JudgePrimeNum(g_p))
    {
        g_p = RandomlyGenerate(3, 255);
    }
    sleep(1);
    g_q = RandomlyGenerate(3, 255);
    while (!JudgePrimeNum(g_q))
    {
        g_q = RandomlyGenerate(3, 255);
    }
    g_n = g_p * g_q;
    int t = (g_p - 1) * (g_q - 1);
    g_e = RandomlyGenerate(2, t);
    while (!RelativePrime(t, g_e))
    {
        g_e = RandomlyGenerate(2, t);
    }
    g_d = CalculateD(g_e, t);
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

//RSA加密,生成密文：5位一组的十进制数字
string encrypt(string s)
{
    string result = "";
    int len = s.length();
    for (int i = 0; i < len; i++)
    {
        int temp = PowerModule(s[i], g_e, g_n);
        int dividend = 10000;
        while (dividend)
        {
            result += (temp / dividend + '0');
            temp %= dividend;
            dividend /= 10;
        }
    }
    return result;
}

//RSA解密,生成明文：字符串
string decrypt(string s)
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
        int temp = PowerModule(c, g_d, g_n);
        result += (char)temp;
    }
    return result;
}
