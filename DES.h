#pragma once
#include <bitset>
#include <iostream>
using namespace std;

bitset<64> key;                // 64位密钥
bitset<48> subKey[16];         // 存放16轮子密钥
bitset<64> plain;              // 存放明文的二进制
bitset<64> cipher;             // 存放密文的二进制
void init(string& s,string& k,int& pattern);  //初始化
void generateKeys();           //生成子密钥
string encrypt(bitset<64>& plain); //加密
string decrypt(bitset<64>& cipher); //解密
