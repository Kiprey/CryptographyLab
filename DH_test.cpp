#include "DH.h"
#include "network.h"
#include <unistd.h>
#include <iostream>
#include <sys/socket.h>
#include <cassert>

#define SYS_ERR(x)  \
    do {            \
        perror(x);  \
        abort();    \
    } while(0)

// 交互用的信息头
#define END_MSG "\x12[QUIT]\x21"

int main(int argc, char *argv[])
{
    // 服务端 [usage] ./DH_test <port>
    if (argc == 2)
    {
        cout << "[SERVER]： 监听端口 " << argv[1] << " ..." << endl;
        int server_fd = socketBindAndListen(atoi(argv[1]));
        if (server_fd < 0)
            SYS_ERR("socketBindAndListen");
        handleSIGPIPE();
        int client_fd;
        if((client_fd = accept(server_fd, nullptr, nullptr)) < 0)
            SYS_ERR("accept");

        // 尝试通信
        Auth_DH dh_service(client_fd);
        dh_service.server_exchange_key();

        string str;
        while(true) {
            str = dh_service.recv();
            if(str == END_MSG)
                break;
            cout << "[MSG from CLIENT] " << str << endl;
            dh_service.send(str);
        }
        dh_service.send(END_MSG);

        close(server_fd);
    }
    // 客户端 [usage] ./DH_test <ip> <port>
    else if(argc == 3)
    {
        cout << "[CLIENT]： 尝试连接 " << argv[1] << ":" << argv[2] << " ..." << endl;
        int client_fd = connect2Server(argv[1], atoi(argv[2]));
        if(client_fd < -1)
            SYS_ERR("connect2Server");
        // 尝试通信
        Auth_DH dh_service(client_fd);
        dh_service.client_exchange_key();

        string str;
        while(cin >> str) {
            dh_service.send(str);
            str = dh_service.recv();
            cout << "[MSG from SERVER] " << str << endl;
        }
        dh_service.send(END_MSG);

        close(client_fd);
    }
    else {
        cout << "服务端 [usage] " << argv[0] << " <port>" << endl;
        cout << "客户端 [usage] " << argv[0] << " <ip> <port>" << endl;
    }

    return 0;
}