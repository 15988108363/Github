from multiprocessing import Process
import sys
from socket import *
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
if __name__=="__main__":
    s= socket()#tcp套接字
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    print("listen 8888:")
    #处理僵尸进程
    #signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    #循环等待客户端连接
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
    #创建新的线程处理客户端请求
        p = Process(target=handle,args=(c,))
        p.daemon = True#主退分支推
        p.start()
