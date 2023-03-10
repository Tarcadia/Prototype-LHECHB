
import socket

ETH_P_IP  = 0x0800
ETH_P_ARP = 0x0806
ETH_P_RARP = 0x8035
ETH_P_ALL = 0x0003

print([socket.PF_PACKET, socket.AF_PACKET])

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s.close()


s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_IP))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s.close()


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s.close()
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
s.bind(("veth0", 0))
x = s.recvfrom(65535)
print(x)
s.close()