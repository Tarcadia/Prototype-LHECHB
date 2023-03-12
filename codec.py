
from random import randbytes
from socket import socket
from base64 import encodebytes
from base64 import decodebytes
from Crypto.Cipher import AES

cryptos = AES.new(b"JESAGFISBKUYDGWE", AES.MODE_ECB) ## HARD CODED FOR TEST ONLY!!!

def recv(conn: socket):
    _lh = ord(conn.recv(1))
    _ll = ord(conn.recv(1))
    _len = _lh * 0xFF + _ll
    assert _len % 16 == 0
    _recv = conn.recv(_len)
    while len(_recv) < _len:
        _recv += conn.recv(_len - len(_recv))
    _recv = cryptos.decrypt(_recv)
    return _recv

def send(conn: socket, data: bytes):
    if len(data) % 16:
        data += randbytes(16 - len(data) % 16)
    _send = cryptos.encrypt(data)
    assert len(_send) <= 0xFFFF and len(_send) % 16 == 0
    _len = len(_send).to_bytes(2, 'big')
    conn.send(_len + _send)
    return
