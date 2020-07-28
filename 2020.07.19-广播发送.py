from socket import *
from time import sleep
#选定广播地址
dest = ("192.168.93.1",9999)
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
date ="""
    **********************************
    5.8 北京 初夏
    喜欢夏天，但你比夏天更明媚
    **********************************
"""
while True:
    sleep(1)
    s.sendto(date.encode(),dest)
s.close()