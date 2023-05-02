#include <sys/socket.h>
#include <linux/in.h>


#define HOST_ADDR "192.168.1.1"
#define HOST_PORT 8888

#define BUFF_SIZE 65536

#define SETTING_INET AF_INET
#define SETTING_PROTO 

int main(int argc, char *argv[])
{
    int sock_o_fd, sock_u_fd;
    char buffer[65536];

    struct sockaddr_in addr;
    sock_o_fd = socket(AF_INET, SOCK_STREAM, 0);
    sock_u_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);

    return 0;
}