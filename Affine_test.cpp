#include "Affine.h"

#include <iostream>

using namespace std;

static string ciphertext; //密文
static string clear_text; //明文

int main()
{
    int quit;  //是否退出程序
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
            affineEncryption(ciphertext);
            cout<<"ciphertext: "<<ciphertext<<endl;
            break;

            //解密
        case 2:
            affineDecryption(clear_text);
            cout<<"clear_text: "<<clear_text<<endl;
            break;
            
        default:
            break;
        }
        cout<<"Enter 0 : quit. Else : continue."<<endl;
        cin>>quit;
        if(!quit)
        break;
    }

    return 1;
}
