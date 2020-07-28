"""gevent协程演示
扩展代码
"""
import gevent
from gevent import monkey
monkey.patch_all()#必须在相应模块导入前导入
from socket import *

def handle(c):
    while True:
        date = c.recv(1024)
        if not date:
            break
        print(date.decode())
        c.send(b"OK")
    c.close()

#创建套接字
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

while True:
    c,addr = s.accept()
    print("connect from：",addr)
    # handle(c)
    gevent.spawn(handle,c)