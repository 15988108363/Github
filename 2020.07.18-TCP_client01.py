"""tcp 客户端"""
from socket import *
sockfd =socket()
server_addr = ("192.168.93.1",8888)#以太网适配器 VMware Network Adapter VMnet1
sockfd.connect(server_addr)
sockfd.send(b"client speak")
date =sockfd.recv(1024)
print("from server",date)
sockfd.close()