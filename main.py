
import socket

# ETH_P_IP  = 0x0800
# ETH_P_ARP = 0x0806
# ETH_P_RARP = 0x8035
# ETH_P_ALL = 0x0003

# print([socket.PF_PACKET, socket.AF_PACKET])

# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
# s.bind(("veth0", 0))
# s.close()
# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
# s.bind(("veth0", 0))
# x = s.recvfrom(65535)
# print(x)
# x = s.recvfrom(65535)
# print(x)
# x = s.recvfrom(65535)
# print(x)
# x = s.recvfrom(65535)
# print(x)
# s.close()


s0 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.bind(("127.0.0.64", 0))
s1.bind(("127.0.0.64", 65534))
# s.bind(("192.168.1.10", 0))
i = 10
while i:
    x = s0.recvfrom(65535)
    print(x[1])
    if x[1] == ("127.0.0.64", 0):
        print(x)
        s1.sendto(x[0][28:], ("127.0.0.64", 0))
        i -= 1
s0.close()
