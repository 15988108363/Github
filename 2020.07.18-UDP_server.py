"""UDP套接字"""
from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("0.0.0.0",8888))
while True:
    date,addr =sockfd.recvfrom(1024)
    print("receive:",date.decode(),addr)
    sockfd.sendto(b"hello",addr)

sockfd.close()