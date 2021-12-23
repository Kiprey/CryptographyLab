#ifndef Affine_H
#define Affine_H

#include <string>
using namespace std;

//只能加密含26个字母的明文！！！

//仿射加密
void affineEncryption(string &ciphertext);

//仿射解密
void affineDecryption(string  &ciphertext);

 #endif
