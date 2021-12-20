#include <iostream>
using namespace std;

/**
 * @brief 绑定和监听某个端口
 * @return 返回 server fd
 */
int socketBindAndListen(int port);

/**
 * @brief 连接 ip:port
 * @return 返回客户端 fd
 */
int connect2Server(const char* ip, int port);

/**
 * @brief 忽视 SIGPIPE 的处理例程，防止程序退出
 */ 
void handleSIGPIPE();

/**
 * @brief 网络交互使用，会检测交互协议等等
 */

void send_msg(int fd, string msg, const char* start_flag, const char* end_flag);
string recv_msg(int fd, const char* start_flag, const char* end_flag);