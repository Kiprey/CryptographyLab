#include <iostream>
#include <fstream>
#include <string>
#include "RSA.cpp"
using namespace std;
int main() 
{
	string s = "Sun Ruijiang is a smart boy";
    ProduceKey();
	fstream file1;
	// 密文写入 cipher.txt
	string cipherS = encrypt(s);
	file1.open("cipher.txt",ios::out);
	file1 << cipherS<<endl;
	file1 << "公钥："<<"("<<g_e<<","<<g_n<<")"<<endl;
	file1 << "私钥："<<"("<<g_d<<","<<g_n<<")"<<endl;
	file1.close();
	// 解密，并写入文件 plain.txt
	string  plainS = decrypt(cipherS,g_d,g_n);
	file1.open("plain.txt",ios::out);
	file1 << plainS;
	file1.close();
	return 0;
}