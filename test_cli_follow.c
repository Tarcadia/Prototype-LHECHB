#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <linux/if.h>
#include <linux/if_tun.h>

#define TUN_DEV "/dev/net/tun"

#define IFNAME "tuntest%d"
#define IFNAME_SIZE sizeof(IFNAME)

#define HOST_ADDR "192.168.1.1"
#define HOST_PORT 8888

int main(int argc, char *argv[]) {
    int tun_fd, sock_fd;
    int err;
    struct ifreq ifr;
    char buffer[65535];

    // 创建TUN设备
    tun_fd = open(TUN_DEV, O_RDWR);
    printf("%d\n", tun_fd);
    memset(&ifr, 0, sizeof(ifr));
    ifr.ifr_flags = IFF_TUN | IFF_NO_PI;
    strncpy(ifr.ifr_name, IFNAME, IFNAME_SIZE);
    err = ioctl(tun_fd, TUNSETIFF, &ifr);
    printf("%d\n", err);

    // while (1) {
    //     // 从TUN设备读取数据
    //     int bytes_read = read(tun_fd, buffer, sizeof(buffer));
    //     for (int i = 0; i <= sizeof(buffer); i++) {
    //         printf("%c", buffer[i]);
    //     }
    // }
    int bytes_read = read(tun_fd, buffer, sizeof(buffer));
    for (int i = 0; i <= sizeof(buffer); i++) {
        printf("%c", buffer[i]);
    }


    sleep(10);

    close(tun_fd);

    return 0;
}