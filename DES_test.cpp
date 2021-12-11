#include <iostream>
#include <fstream>
#include <bitset>
#include <string>
#include "DES.cpp"
using namespace std;
int main() 
{
	string s = "Secret!?";
	string k = "12345678";
    int pattern = 0;
	init(s,k,pattern);
	// 生成16个子密钥
	generateKeys();   
	fstream file1;
	// 密文写入 cipher.txt
	string cipherS = encrypt(plain);
	file1.open("cipher.txt",ios::out);
	file1 << cipherS;
	file1.close();
	// 解密，并写入文件 plain).txt
	pattern = 1;
	init(cipherS,k,pattern);
	string  plainS = decrypt(cipher);
	file1.open("plain.txt",ios::out);
	file1 << plainS;
	file1.close();
	return 0;
}