
from socket import socket
from base64 import encodebytes
from base64 import decodebytes
from Crypto.Cipher import AES

cryptos = AES.new(b"JESAGFISBKUYDGWE", AES.MODE_ECB) ## HARD CODED FOR TEST ONLY!!!

def recv(conn: socket):
    _lh = ord(conn.recv(1))
    _ll = ord(conn.recv(1))
    _len = _lh * 0xFF + _ll
    _recv = conn.recv(_len)
    while len(_recv) < _len:
        _recv += conn.recv(_len - len(_recv))
    _recv = cryptos.decrypt(decodebytes(_recv))
    return _recv

def send(conn: socket, data: bytes):
    _send = encodebytes(cryptos.encrypt(data))
    assert len(_send) <= 0xFFFF
    _len = len(_send).to_bytes(2, 'big')
    conn.send(_len + _send)
    return
