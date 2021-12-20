#include <iostream>
#include <fstream>
#include <bitset>
#include <string>
#include "DES.h"
using namespace std;
int main() 
{
	string s = "It's a secret?";
	string k = "12345678";
	// 生成16个子密钥
	generateKeys(k);   
	fstream file1;
	// 密文写入 cipher.txt
	string cipherS = encrypt(s);
	file1.open("cipher.txt",ios::out);
	file1 << cipherS;
	file1.close();
	// 解密，并写入文件 plain.txt
	string  plainS = decrypt(cipherS);
	file1.open("plain.txt",ios::out);
	file1 << plainS;
	file1.close();
	return 0;
}