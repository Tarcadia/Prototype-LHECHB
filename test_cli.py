
import string
import random
import socket
import codec
import threading

ETH_P_IP  = 0x0800
ETH_P_ARP = 0x0806
ETH_P_RARP = 0x8035
ETH_P_ALL = 0x0003

IFACE = "veth1"

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("host-bj-00.tarcadia.net", 64444))

verify_key = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 64)).encode("UTF-8")
codec.send(conn, verify_key)
inlet_key = codec.recv(conn)
print(inlet_key)
if inlet_key[:64] != verify_key:
    exit()
outlet_key = inlet_key[64:]
codec.send(conn, outlet_key)

print("connected")

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_IP))
s.bind((IFACE, 0))
s.close()
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_IP))
s.bind((IFACE, 0))

def run_ingress():
    while True:
        _data, _from = s.recvfrom(9000)
        if len(_from) >= 3 and _from[0] == IFACE and _from[1] == 2048 and _from[2] in (0, 1, 2):
            codec.send(conn, _data)

def run_egress():
    while True:
        _data = codec.recv(conn)
        s.send(_data)

thr_ingress = threading.Thread(target = run_ingress, name = "thr_ingress")
thr_egress = threading.Thread(target = run_egress, name = "thr_egress")
thr_ingress.start()
thr_egress.start()

while True:
    pass