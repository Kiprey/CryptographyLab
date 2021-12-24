#include "Affine.h"

#include <iostream>

using namespace std;

int main()
{
    string ciphertext; //密文
    string clear_text; //明文
    int key1, key2;    //两个密钥
    int quit;          //是否退出程序
    while (1)
    {
        //选择加密或者解密
        int choice;
        while (1)
        {
            cout << "Please choose modren. 1.encrypt 2.decrypt" << endl;
            cin >> choice;
            if (choice == 1 || choice == 2)
                break;
            else
                cout << "Invalid input!" << endl;
        }

        switch (choice)
        {
            //加密
        case 1:
            while (1)
            {
                cout << " Please enter plaintext!" << endl;
                cout<< "Note: Only 26 letters can be encrypted!"<<endl;
                char c = cin.get(); //读取多余的回车符
                getline(cin, clear_text);
                //保证输入不为空
                if (clear_text == "")
                    cout << "The plaintext is empty! Please enter again. " << endl;
                else
                    break;
            }
            while (1)
            {
                cout << " Please enter key1,key2!" << endl;
                cout<< "Note: key1 must be prime with 26 and 0<=key2<26!"<<endl;
                cin >> key1 >> key2;
                //key1，key2可用,进行加密，否则重新输入key1，key2
                if (affineEncryption(key1, key2, clear_text, ciphertext))
                    break;
                else
                    cout << "Invalid input! Please enter again. " << endl;
            }

            cout << "ciphertext: " << ciphertext << endl;
            break;

            //解密
        case 2:
            while (1)
            {
                cout << " Please enter ciphertext!" << endl;
                char c = cin.get(); //读取多余的回车符
                getline(cin, ciphertext);
                //保证输入不为空
                if (ciphertext == "")
                    cout << "The ciphertext is empty! Please enter again. " << endl;
                else
                    break;
            }
            while (1)
            {
                cout << " Please enter key1,key2!" << endl;
                cin >> key1 >> key2;
                //key1，key2可用,进行解密，否则重新输入key1，key2
                if (affineDecryption(key1, key2, ciphertext, clear_text))
                    break;
                else
                    cout << "Invalid input! Please enter again. " << endl;
            }

            cout << "clear_text: " << clear_text << endl;
            break;

        default:
            break;
        }
        cout << "Enter 0 : quit. Else : continue." << endl;
        cin >> quit;
        if (!quit)
            break;
    }

    return 1;
}
