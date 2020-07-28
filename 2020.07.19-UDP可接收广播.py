#1，创建UDP套接字
# 2.设置套接字为可接收广播
# 3,选择接收端口
from socket import *
s01 = socket(AF_INET,SOCK_DGRAM)
#让套接字可以接收广播
s01.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s01.bind(("0.0.0.0",9999))
while True:
    try:
        msg,addr =s01.recvfrom(1024)
    except KeyboardInterrupt:
        break
    else:
        print(msg.decode())
s01.close()