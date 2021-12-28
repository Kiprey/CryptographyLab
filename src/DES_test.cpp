#include <iostream>
#include <fstream>
#include <bitset>
#include <string>
#include "DES.h"
using namespace std;
int main() 
{
	string key;
	cout << "Key: ";
	cin >> key;

	string data;
	cout << "data: ";
	cin >> data;
	// 生成16个子密钥
	generateKeys(key);   
	string cipher = encrypt(data);
	cout << "enc_cipher: " << cipher << endl;
	generateKeys(key);   
	string  plain = decrypt(cipher);
	cout << "dec_plain: " << plain << endl;
	return 0;
}