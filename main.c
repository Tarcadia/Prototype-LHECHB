#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <net/if.h>
#include <errno.h>

int main()
{
    int sock;
    struct sockaddr_in addr, raddr;
    char buffer[] = "Hello";
    struct ifreq nif;
    char *inface = "veth0";
    strcpy(nif.ifr_name, inface);

    sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
    if (sock == -1)
    {
        printf("Fail creating socket.\n");
        return 1;
    }
    if (inet_aton("0.0.0.0", &addr.sin_addr) != 1)
    {
        printf("Fail creating addr.\n");
        return 1;
    }
}