#ifndef Affine_H
#define Affine_H

#include <string>
using namespace std;

//只能加密含26个字母的明文！！！

/*
仿射加密
key1,key2为两个密钥，key1必须与26互素，key2的范围[0,26)
plaintext为需要加密的明文，ciphertext为加密后的密文
如果输入的key1，key2合法则进行加密并返回1，不合法返回0
*/
bool affineEncryption(int key1, int key2,string plaintext,string &ciphertext);

//仿射解密，含义与加密函数相同
bool affineDecryption(int key1,int key2,string ciphertext,string &clear_text);

 #endif
