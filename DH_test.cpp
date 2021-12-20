#include "DH.h"
#include "network.h"
#include <unistd.h>
#include <iostream>
#include <sys/socket.h>
#include <cassert>

// 交互用的信息头
#define END_MSG "\x12[QUIT]\x21"

int main(int argc, char *argv[])
{
    // 服务端 [usage] ./DH_test <port>
    if (argc == 2)
    {
        int server_fd = socketBindAndListen(atoi(argv[1]));
        if (server_fd < 0)
            perror("socketBindAndListen");
        handleSIGPIPE();
        int client_fd = accept(server_fd, nullptr, nullptr);
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
    else
    {
        assert(argc > 2);
        int client_fd = connect2Server(argv[1], atoi(argv[2]));
        if(client_fd < -1)
            perror("connect2Server");
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

    return 0;
}