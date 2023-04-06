import socket
from threading import Thread
from pynput.keyboard import Key,Controller
from screeninfo import get_monitors

SERVER = None
PORT = 5500
IP_ADDRESS = '192.168.1.7'
screen_width = None
screen_height = None


keyboard = Controller()

def acceptConnections():
    while True:
      client_socket,addr = SERVER.accept()
      print("Connection established with {client_socket}: {addr}")

      thread = Thread(target=recvMessage,args=client_socket)
      thread.start() 
            
    
def get_screenSize():
   global screen_width
   global screen_height

   for m in get_monitors():
      screen_width = int(str(m).split[','][2].strip().split["width="][1])
      screen_height = int(str(m).split[','][3].strip().split["height="][1])

def recvMessage(client_socket):
   global keyboard

   while True:
      try :
         message = client_socket.recv(2048).decode()
         if(message):
            keyboard.press(message)
            keyboard.release(message)
            print(message)
      except Exception as error:
           pass
            

def setup():
    print('/n/n/Welcome to Remote Keyboard Server')
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(10)
    acceptConnections()
    get_screenSize()
    print('/n/n/n/*****SERVER IS WAITING FOR INCOMING CONNECTIONS*****/n')

setup()