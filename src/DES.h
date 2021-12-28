#pragma once
#include <bitset>
#include <iostream>
using namespace std;

void generateKeys(string& k);    // 生成子密钥
// 由于密文转字符容易乱码。故明文为普通字符串，密文为二进制位组成的字符串
string encrypt(string &s);       // 加密函数
string decrypt(string &s);       // 解密函数
