#include "LFSR.h"
#include <iostream>

//编码，将字符串转换为十六进制
string encode(string data)
{
    //编码表
    const char Encode_Table[] = "0123456789ABCDEF";
    //返回值
    string str_encode;
    unsigned char Tmp = {0};
    unsigned int len = data.length();
    for (int i = 0; i < len; i++)
    {
        Tmp = data[i];
        str_encode += Encode_Table[Tmp >> 4];   // 处理高位
        str_encode += Encode_Table[Tmp & 0x0f]; //处理低4位
    }
    return str_encode;
}

//解码，将十六进制字符串转换为字符串
string decode(string data)
{
    unsigned int len = data.length();
    string str_dncode(len/2,'1');
    for (int i = 0; i < len / 2; i++)
    {
        int tmp1 = (int)data[i * 2] - (((int)data[i * 2] >= 'A') ? 'A' - 10 : '0');
        if (tmp1 >= 16)
            return NULL;
        int tmp2 = (int)data[i * 2 + 1] - (((int)data[i * 2 + 1] >= 'A') ? 'A' - 10 : '0');
        if (tmp2 >= 16)
            return NULL;
        str_dncode[i]= (tmp1 * 16 + tmp2);
    }
    return str_dncode;
}

int main()
{
    unsigned char c[4]; //反馈系数
    string key;           //密钥
    string data;          //明文或者密文

    int choice;        //选择加密或者解密
    while (1)
    {
        cout << "Please choose modren. 1.encrypt 2.decrypt" << endl;
        cin >> choice;
        if (choice == 1 || choice == 2)
            break;
        else
            cout << "Invalid input!" << endl;
    }

    //获取密钥
    while (1)
    {
        cout << " Please enter the key!" << endl;
        char c = cin.get(); //读取多余的回车符
        getline(cin, key);
        //保证输入不为空
        if (key == "")
            cout << "The key is empty! Please enter again. " << endl;
        else
            break;
    }

    coefInit(c,key); //根据密钥初始化反馈系数

    //获取明文或者密文
    while (1)
    {
        if (choice == 1)
        {
            cout << " Please enter the plaintext!" << endl;
        }
        else
            cout << " Please enter the ciphertext!" << endl;
        // char c = cin.get(); //读取多余的回车符
        getline(cin, data);
        //保证输入不为空
        if (data == "")
            cout << "Data is empty! Please enter again. " << endl;
        else
            break;
    }
    //加密
    if (choice == 1)
    {
        cout << encode(LFSR(data,c)) << endl;
    }

    //解密
    else
    {
        cout << LFSR(decode(data),c) << endl;
    }
    
    return 0;
}