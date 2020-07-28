from socket import *
import os,sys
import signal
#创建监听套接字
HOST = "0.0.0.0"
PORT = 8888
ADDR =(HOST,PORT)

def handle(c):
    print("client_addr:",c.getpeername())
    while True:
        date = c.recv(1024)
        if not date:
            break
        print(date.decode())
        c.send(b"OK")
    c.close()

s= socket()#tcp套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#僵尸进程的处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("listen 8888:")
#循环等待客户端连接
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    #创建子进程处理客户端请求
    pid = os.fork()
    if pid==0:
        s.close()#子进程不需要s
        handle(c)#处理客户端连接
        os._exit(0)
        #父进程实际只用来处理客户端连接
    else:
        c.close()#父进程不需要c

