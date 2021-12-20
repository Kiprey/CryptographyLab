#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <cassert>
#include <cstring>
#include <csignal>
#include "network.h"

int socketBindAndListen(int port)
{
    int listen_fd = 0;
    // 开始创建 socket, 注意这是阻塞模式的socket
    // AF_INET      : IPv4 Internet protocols
    // SOCK_STREAM  : TCP socket
    if ((listen_fd = socket(AF_INET, SOCK_STREAM | SOCK_NONBLOCK | SOCK_CLOEXEC, 0)) == -1)
        return -1;

    // 绑定端口
    sockaddr_in server_addr;
    // 初始化一下
    memset(&server_addr, '\0', sizeof(server_addr));
    // 设置一下基本操作
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons((unsigned short)port);
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    // 端口复用
    int opt = 1;
    if (setsockopt(listen_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) == -1)
        return -1;
    // 试着bind
    if (bind(listen_fd, (sockaddr *)&server_addr, sizeof(server_addr)) == -1)
        return -1;
    // 试着listen, 设置最大队列长度为 1024
    if (listen(listen_fd, 1024) == -1)
        return -1;

    return listen_fd;
}

int connect2Server(const char *ip, int port)
{
    // 获得socket
    int fd = socket(AF_INET, SOCK_STREAM, 0);

    // 设置需要连接的ip端口
    struct sockaddr_in sock_addr;
    // 初始化
    memset(&sock_addr, 0, sizeof(sock_addr));
    // 设置连接协议、连接端口和连接地址
    sock_addr.sin_family = AF_INET;
    sock_addr.sin_port = htons(port); /*将端口转化成网络字节序 */
                                      //将命令行读入的字符串ip转化成能用的ip
    if (inet_aton(ip, &sock_addr.sin_addr) == 0)
        return -1;
    // 最后连接
    return connect(fd, (const struct sockaddr *)&sock_addr, sizeof(struct sockaddr)); //建立连接
}

void handleSIGPIPE()
{
    struct sigaction sa;
    memset(&sa, '\0', sizeof(sa));
    sa.sa_handler = SIG_IGN;
    sa.sa_flags = 0;
    if (sigaction(SIGPIPE, &sa, NULL) == -1)
        perror("Ignore SIGPIPE");
}

void send_msg(int fd, string msg, const char* start_flag, const char* end_flag) {
    string send_msg = start_flag + msg + end_flag;
    ssize_t ret = send(fd, send_msg.c_str(), send_msg.size(), 0);
    assert(ret == send_msg.size());
}

string recv_msg(int fd, const char* start_flag, const char* end_flag) {
    string msg;
    // 一直接收，直到接收到了 MSG FLAG
    while(msg.find(end_flag) == string::npos) {
        char ch;
        ssize_t ret;

        if((ret = recv(fd, &ch, 1, MSG_DONTWAIT)) < 0)
        {
            if(errno != EINTR && errno != EAGAIN)
                return string();
        }
        else if(ret == 1)
            msg += ch;
        // 其他情况下直接break掉，防止死循环。
        else
            break;
    }
    // 检测消息完整
    const size_t start_flag_len = strlen(start_flag);
    const size_t end_flag_len = strlen(end_flag);
    assert(msg.substr(0, start_flag_len) == start_flag);
    assert(msg.substr(msg.size() - end_flag_len) == end_flag);
    // 返回除去消息头的信息
    return msg.substr(start_flag_len, msg.size() - end_flag_len - start_flag_len);
}