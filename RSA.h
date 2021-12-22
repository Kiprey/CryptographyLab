#pragma once
#include <string>
#include <iostream>
using namespace std;
string encrypt(string s); //RSA加密,生成密文：5位一组的十进制数字
string decrypt(string s); //RSA解密,需要输入私钥,生成明文：字符串
