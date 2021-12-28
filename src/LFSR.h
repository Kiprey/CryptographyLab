#ifndef LFSR_H
#define LFSR_H

#include <string>
#include <bitset>
using namespace std;

//本次使用4个寄存器储存密钥输出流

/*
初始化反馈系数
*/
void coefInit(unsigned char *c, string key);

//加解密函数
string LFSR(string data,unsigned char *c);

 #endif
