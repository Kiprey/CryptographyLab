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
