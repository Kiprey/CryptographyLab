#include "Affine.h"
#include <algorithm>
#include <iostream>
#include <cctype>

static int gcd(int s, int t)
{
    if (t == 0)
    {
        return s;
    }
    return gcd(t, s % t);
}

static int exgcd(int a, int b, int &x, int &y)
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

static int calInverse(int a, int m)
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

void affineEncryption(string &ciphertext)
{
    string plaintext; //明文
    int key1, key2;   //密钥1，密钥2
    while (1)
    {
        cout << " Please enter plaintext!" << endl;
        char c = cin.get(); //读取多余的回车符
        getline(cin, plaintext);
        //保证输入不为空
        if (plaintext == "")
            cout << "The plaintext is empty! Please enter again. " << endl;
        else
            break;
    }
    while (1)
    {
        cout << " Please enter key1,key2!" << endl;
        cin >> key1 >> key2;
        //key1，key2可用
        if (gcd(26, key1) == 1 && key1 >= 0 && key2 >= 0 && key1 < 26 && key2 < 26)
            break;
        else
            cout << "Invalid input! Please enter again. " << endl;
    }
    ciphertext = ""; //清空密文
    for (int i = 0; i < plaintext.length(); i++)
    {
        if (isalpha(plaintext[i]))//处理字母
        {
            if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')//将大写字母转换为小写字母
                plaintext[i] = plaintext[i] + 32;
            int code = plaintext[i] - 'a';    //字符变数字
            code = (key1 * code + key2) % 26; //加密 c=am+b mod 26
            char temp = code + 'a';           //数字变字符
            ciphertext = ciphertext + temp;   //得到密文
        }
    }
}

void affineDecryption(string &clear_text)
{
    string g_ciphertext; //密文
    int key1, key2;      //密钥1，密钥2
    while (1)
    {
        cout << " Please enter ciphertext!" << endl;
        char c = cin.get(); //读取多余的回车符
        getline(cin, g_ciphertext);
        //保证输入不为空
        if (g_ciphertext == "")
            cout << "The ciphertext is empty! Please enter again. " << endl;
        else
            break;
    }
    while (1)
    {
        cout << " Please enter key1,key2!" << endl;
        cin >> key1 >> key2;
        //key1，key2可用
        if (gcd(26, key1) == 1 && key1 >= 0 && key2 >= 0 && key1 < 26 && key2 < 26)
            break;
        else
            cout << "Invalid input! Please enter again. " << endl;
    }
    clear_text = ""; //清空明文
    for (int i = 0; i < g_ciphertext.length(); i++)
    {
        int code = g_ciphertext[i] - 'a'; //字符变数字
        //解密 m=(c-b+n)*a^(-1) mod n
        code = ((code - key2 + 26) * calInverse(key1, 26)) % 26;
        char temp = code + 'a';         //数字变字符
        clear_text = clear_text + temp; //得到明文
    }
}