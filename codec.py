
from socket import socket
from base64 import encodebytes
from base64 import decodebytes
from Crypto.Cipher import AES

cryptos = AES.new("JESAGFISBKUYDGWE", AES.MODE_ECB) ## HARD CODED FOR TEST ONLY!!!

def recv(conn: socket):
    _lh = conn.recv(1)
    _ll = conn.recv(1)
    _len = _lh * 0xFF + _ll
    _recv = conn.recv(_len)
    while len(_recv) < _len:
        _recv += conn.recv(len(_recv) - _len)
    _recv = cryptos.decrypt(decodebytes(_recv))
    return _recv

def send(conn: socket, data: bytes):
    _send = encodebytes(cryptos.encrypt(data))
    _len = len(_send)
    assert _len <= 0xFFFF
    _lh, _ll = _len // 256, _len % 256
    conn.send(bytes([_lh, _ll]) + _send)
    return
