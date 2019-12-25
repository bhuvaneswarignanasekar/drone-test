import threading 
import socket
import sys
import time
import platform

class Drone:
    is_connected=False
   

    def __init__(self):
        self.host = '192.168.10.3'
        self.port = 9000
        self.locaddr = (self.host,self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)

    def connect(self):
        self.msg="command"
        self.is_connected="true"
        self.msg = self.msg.encode(encoding="utf-8") 
        sent = self.sock.sendto(self.msg, self.tello_address)
        print("Message sent to Tello"+str(self.msg))
        return sent
    
    def command(self,command):
        self.msg=command
        self.is_connected="true"
        self.msg = self.msg.encode(encoding="utf-8") 
        sent = self.sock.sendto(self.msg, self.tello_address)
        print("Message sent to Tello"+str(self.msg))
        return sent