#include <iostream>
#include <fstream>
#include <string>
#include "RSA.h"
using namespace std;
int main()
{
	string s = "Sun Ruijiang is a smart boy";
	fstream file1;
	key k;
	k = ProduceKey();
	// 密文写入 cipher.txt
	string cipherS = publicEncrypt(s, k);
	file1.open("cipher.txt", ios::out);
	file1 << cipherS << endl;
	file1 << "公钥："
		  << "(" << k.e << "," << k.n << ")" << endl;
	file1 << "私钥："
		  << "(" << k.d << "," << k.n << ")" << endl;
	file1.close();
	// 解密，并写入文件 plain.txt
	string plainS = privateDecrypt(cipherS, k);
	file1.open("plain.txt", ios::out);
	file1 << plainS;
	file1.close();
	return 0;
}