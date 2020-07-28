"""tcp 客户端"""
from socket import *
sockfd =socket()
server_addr = ("192.168.0.105",8888)
#无线网适配器 WLAN
#地址随路由器重启改变，用cmd中ipconfig指令修改绑定地址
sockfd.connect(server_addr)
sockfd.send(b"client speak")
date =sockfd.recv(1024)
print("from server",date)
sockfd.close()