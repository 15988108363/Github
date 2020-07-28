from socket import *
sockfd =socket(AF_INET,SOCK_DGRAM)
server_addr = ("192.168.43.195",8888)
HOST ="192.168.43.195"
PORT =8888
ADDR=(HOST,PORT)
while True:
    date = input("message")
    if not date:
        break
    sockfd.sendto(date.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("from server:",msg.decode())
sockfd.close()