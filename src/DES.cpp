#include <iostream>
#include <bitset>
#include "DES.h"
using namespace std;

static bitset<48> g_sub_key[16];					  // 存放16轮子密钥
static bitset<32> f(bitset<32> R, bitset<48> k);	  //密码函数（乘积变换）f
static bitset<28> leftShift(bitset<28> k, int shift); //对56位密钥的前后部分进行左移
static bitset<64> charToBitset(const char s[8]);	  //将char字符数组转为二进制
static string bitsetToString(bitset<64> bits);		  //将二进制转为字符串
static int hexToInt(char ch);						  //十六进制字符转十进制数
static string encryptOnce(bitset<64> &plain);		  //单次64位加密
static string decryptOnce(bitset<64> &cipher);		  //单次64位解密

// 初始置换表
static const int IP[] = {58, 50, 42, 34, 26, 18, 10, 2,
						 60, 52, 44, 36, 28, 20, 12, 4,
						 62, 54, 46, 38, 30, 22, 14, 6,
						 64, 56, 48, 40, 32, 24, 16, 8,
						 57, 49, 41, 33, 25, 17, 9, 1,
						 59, 51, 43, 35, 27, 19, 11, 3,
						 61, 53, 45, 37, 29, 21, 13, 5,
						 63, 55, 47, 39, 31, 23, 15, 7};

// 结尾置换表
static const int IP_1[] = {40, 8, 48, 16, 56, 24, 64, 32,
						   39, 7, 47, 15, 55, 23, 63, 31,
						   38, 6, 46, 14, 54, 22, 62, 30,
						   37, 5, 45, 13, 53, 21, 61, 29,
						   36, 4, 44, 12, 52, 20, 60, 28,
						   35, 3, 43, 11, 51, 19, 59, 27,
						   34, 2, 42, 10, 50, 18, 58, 26,
						   33, 1, 41, 9, 49, 17, 57, 25};

/*------------------下面是生成密钥所用表-----------------*/

// 置换选择PC1
static const int PC_1[] = {57, 49, 41, 33, 25, 17, 9,
						   1, 58, 50, 42, 34, 26, 18,
						   10, 2, 59, 51, 43, 35, 27,
						   19, 11, 3, 60, 52, 44, 36,
						   63, 55, 47, 39, 31, 23, 15,
						   7, 62, 54, 46, 38, 30, 22,
						   14, 6, 61, 53, 45, 37, 29,
						   21, 13, 5, 28, 20, 12, 4};

// 置换选择PC2
static const int PC_2[] = {14, 17, 11, 24, 1, 5,
						   3, 28, 15, 6, 21, 10,
						   23, 19, 12, 4, 26, 8,
						   16, 7, 27, 20, 13, 2,
						   41, 52, 31, 37, 47, 55,
						   30, 40, 51, 45, 33, 48,
						   44, 49, 39, 56, 34, 53,
						   46, 42, 50, 36, 29, 32};

// 每轮左移的位数
static const int shiftBits[] = {1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1};

/*------------------下面是密码函数(乘积变换)f 所用表-----------------*/

// 扩展置换表，将 32位 扩展至 48位
static const int E[] = {32, 1, 2, 3, 4, 5,
						4, 5, 6, 7, 8, 9,
						8, 9, 10, 11, 12, 13,
						12, 13, 14, 15, 16, 17,
						16, 17, 18, 19, 20, 21,
						20, 21, 22, 23, 24, 25,
						24, 25, 26, 27, 28, 29,
						28, 29, 30, 31, 32, 1};

// S盒，每个S盒是4x16的置换表，6位 -> 4位
static const int S_BOX[8][4][16] = {
	{{14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7},
	 {0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8},
	 {4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0},
	 {15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13}},
	{{15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10},
	 {3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5},
	 {0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15},
	 {13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9}},
	{{10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8},
	 {13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1},
	 {13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7},
	 {1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12}},
	{{7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15},
	 {13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9},
	 {10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4},
	 {3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14}},
	{{2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9},
	 {14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6},
	 {4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14},
	 {11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3}},
	{{12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11},
	 {10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8},
	 {9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6},
	 {4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13}},
	{{4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1},
	 {13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6},
	 {1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2},
	 {6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12}},
	{{13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7},
	 {1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2},
	 {7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8},
	 {2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11}}};

// 用于P置换，32位 -> 32位
static const int P[] = {16, 7, 20, 21,
						29, 12, 28, 17,
						1, 15, 23, 26,
						5, 18, 31, 10,
						2, 8, 24, 14,
						32, 27, 3, 9,
						19, 13, 30, 6,
						22, 11, 4, 25};
//十六进制字符表
static const char Hex[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
//十六进制字符转十进制数
int hexToInt(char ch)
{
	if ('0' <= ch && ch <= '9')
	{
		return (ch - '0');
	}
	else if ('a' <= ch && ch <= 'f')
	{
		return (10 + ch - 'a');
	}
	else
	{
		return -1;
	}
}

/*                            下面是DES算法实现                         */
//乘积变换f，接收32位数据和48位子密钥，产生一个32位的输出
bitset<32> f(bitset<32> R, bitset<48> k)
{
	bitset<48> expandR;
	// 第一步：选择扩展运算E，32->48
	for (int i = 0; i < 48; ++i)
		expandR[47 - i] = R[32 - E[i]];
	// 第二步：异或（模2相加）
	expandR = expandR ^ k;
	// 第三步：选择压缩运算S，48->32
	bitset<32> output;
	int x = 0;
	for (int i = 0; i < 48; i = i + 6)
	{
		//首位2位决定行，中间4位决定列
		int row = expandR[47 - i] * 2 + expandR[47 - i - 5];
		int col = expandR[47 - i - 1] * 8 + expandR[47 - i - 2] * 4 + expandR[47 - i - 3] * 2 + expandR[47 - i - 4];
		int num = S_BOX[i / 6][row][col];
		bitset<4> binary(num);
		output[31 - x] = binary[3];
		output[31 - x - 1] = binary[2];
		output[31 - x - 2] = binary[1];
		output[31 - x - 3] = binary[0];
		x += 4;
	}
	// 第四步：置换运算P，32->32
	bitset<32> tmp = output;
	for (int i = 0; i < 32; ++i)
		output[31 - i] = tmp[32 - P[i]];
	return output;
}

// 对56位密钥的前后部分进行左移
bitset<28> leftShift(bitset<28> k, int shift)
{
	bitset<28> tmp = k;
	for (int i = 27; i >= 0; --i)
	{
		if (i - shift < 0)
			k[i] = tmp[i - shift + 28];
		else
			k[i] = tmp[i - shift];
	}
	return k;
}

//工具函数：将char字符数组转为二进制（64位）
bitset<64> charToBitset(const char s[8])
{
	bitset<64> bits;
	for (int i = 0; i < 8; ++i)
		for (int j = 0; j < 8; ++j)
			bits[i * 8 + j] = ((s[i] >> j) & 1);
	return bits;
}

// 工具函数：将（64位）二进制转为字符串
string bitsetToString(bitset<64> bits)
{
	char *s;
	s = (char *)&bits;
	string result = "";
	for (int i = 0; i < 8; ++i)
		result += s[i];
	cout << result << endl;
	return result;
}

// 生成16个48位的子密钥
void generateKeys(string &k)
{
	bitset<64> key = charToBitset(k.c_str()); // 64位密钥
	bitset<56> realKey;
	bitset<28> left;
	bitset<28> right;
	bitset<48> compressKey;
	// 去掉奇偶标记位，将64位密钥变成56位
	for (int i = 0; i < 56; ++i)
		realKey[55 - i] = key[64 - PC_1[i]];
	// 生成子密钥，保存在 subKeys[16]中
	for (int round = 0; round < 16; ++round)
	{
		// 前28位与后28位
		for (int i = 28; i < 56; ++i)
			left[i - 28] = realKey[i];
		for (int i = 0; i < 28; ++i)
			right[i] = realKey[i];
		// 左移
		left = leftShift(left, shiftBits[round]);
		// 右移
		right = leftShift(right, shiftBits[round]);
		// 压缩置换，由56位得到48位子密钥
		for (int i = 28; i < 56; ++i)
			realKey[i] = left[i - 28];
		for (int i = 0; i < 28; ++i)
			realKey[i] = right[i];
		for (int i = 0; i < 48; ++i)
			compressKey[47 - i] = realKey[56 - PC_2[i]];
		g_sub_key[round] = compressKey;
	}
}

// 单次DES加密（8位字符->16位16进制）
string encryptOnce(string s)
{
	string result = "";
	bitset<64> plain = charToBitset(s.c_str());
	bitset<64> temp_cipher;
	bitset<64> current_bits;
	bitset<32> left;
	bitset<32> right;
	bitset<32> new_left;
	// 第一步：初始置换IP
	for (int i = 0; i < 64; ++i)
		current_bits[63 - i] = plain[64 - IP[i]];
	// 第二步：获取 Li 和 Ri，进行十六轮迭代（在子密钥控制下的乘积变换）
	for (int i = 32; i < 64; ++i)
		left[i - 32] = current_bits[i];
	for (int i = 0; i < 32; ++i)
		right[i] = current_bits[i];
	for (int round = 0; round < 16; ++round)
	{
		new_left = right;
		right = left ^ f(right, g_sub_key[round]);
		left = new_left;
	}
	// 第三步：合并L32和R32，注意交换左右32位比特，合并为R32L32
	for (int i = 0; i < 32; ++i)
		temp_cipher[i] = left[i];
	for (int i = 32; i < 64; ++i)
		temp_cipher[i] = right[i - 32];
	// 第四步：初始逆置换IP^(-1)
	current_bits = temp_cipher;
	for (int i = 0; i < 64; ++i)
		temp_cipher[63 - i] = current_bits[64 - IP_1[i]];
	// 将64位二进制的密文转化为16个十六进制数组成的字符串
	for (int i = 0; i < 64; i += 4)
	{
		int pos;
		pos = temp_cipher[i] * 8 + temp_cipher[i + 1] * 4 + temp_cipher[i + 2] * 2 + temp_cipher[i + 3];
		result += Hex[pos];
	}
	return result;
}

// 单次DES解密（16位16进制->8位字符）
string decryptOnce(string s)
{
	string result;
	bitset<64> cipher;
	int s_len = s.length();
	// 将16个十六进制数组成的字符串转化为64位二进制
	for (int i = 0; i < s_len; i++)
	{
		int num = hexToInt(s[i]);
		if (num == -1)
		{
			result = "Input error.";
			return result;
		}
		int divide = 8;
		for (int j = 0; j < 4; j++)
		{
			cipher[i * 4 + j] = num / divide;
			num -= cipher[i * 4 + j] * divide;
			divide /= 2;
		}
	}
	cout << cipher.to_string();
	bitset<64> temp_plain;
	bitset<64> current_bits;
	bitset<32> left;
	bitset<32> right;
	bitset<32> new_left;
	// 第一步：初始置换IP
	for (int i = 0; i < 64; ++i)
		current_bits[63 - i] = cipher[64 - IP[i]];
	// 第二步：获取 Li 和 Ri
	for (int i = 32; i < 64; ++i)
		left[i - 32] = current_bits[i];
	for (int i = 0; i < 32; ++i)
		right[i] = current_bits[i];
	// 第三步：共16轮迭代（子密钥逆序应用）
	for (int round = 0; round < 16; ++round)
	{
		new_left = right;
		right = left ^ f(right, g_sub_key[15 - round]);
		left = new_left;
	}
	// 第四步：合并L32和R32，注意合并为：R32L32
	for (int i = 0; i < 32; ++i)
		temp_plain[i] = left[i];
	for (int i = 32; i < 64; ++i)
		temp_plain[i] = right[i - 32];
	// 第五步：结尾置换IP-1
	current_bits = temp_plain;
	for (int i = 0; i < 64; ++i)
		temp_plain[63 - i] = current_bits[64 - IP_1[i]];
	//二进制串转化为字符串
	result = bitsetToString(temp_plain);
	cout << result << endl;
	// 返回明文
	return result;
}

// 加密函数（目标：字符串）
string encrypt(string &s)
{
	string result = "";
	string sub_s;
	int len = s.length();
	for (int i = 0; i < len; i += 8)
	{
		sub_s = s.substr(i, 8);
		result += encryptOnce(sub_s);
	}
	return result;
}
// 解密函数（目标：十六进制字符串）
string decrypt(string &s)
{
	string result = "";
	string sub_s;
	int len = s.length();
	for (int i = 0; i < len; i += 16)
	{
		sub_s = s.substr(i, 16);
		result += decryptOnce(sub_s);
		cout << result << endl;
	}
	int pos = len / 2; //'\00'的最先位置
	for (int i = len / 2 - 1; i >= 0; i--)
	{
		if (result[i] != '\00')
		{
			pos = i + 1;
			break;
		}
	}
	return result.substr(0, pos);
}