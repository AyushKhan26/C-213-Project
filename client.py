import socket
from threading import Thread

SERVER = None
PORT = 5500
IP_ADDRESS = ' 192.168.1.7'

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect(IP_ADDRESS,PORT)

setup() 