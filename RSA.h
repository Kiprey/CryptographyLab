#pragma once
#include <string>
#include <iostream>
using namespace std;
void ProduceKey();              //产生密钥
string encrypt(string s); //RSA加密,生成密文：5位一组的十进制数字
string decrypt(string s); //RSA解密,生成明文：字符串
