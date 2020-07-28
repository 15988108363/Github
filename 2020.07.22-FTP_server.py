"""ftp文件服务器"""
#-*-coding:utf-8-*
from socket import *
from threading import Thread
import os,time
#全局变量
HOST ="0.0.0.0"
PORT =8888
ADDR = (HOST,PORT)
Filepath = """D:\PyCharm——练习文件\临时文件\\"""
#将客户端请求封装成类
class FtpServer:
    def __init__(self,connfd,path):
        self.connfd=connfd
        self.path =path
    def do_list(self):
        files=os.listdir(self.path)
        if not files:
            self.connfd.send("empty".encode())
            return
        else:
            self.connfd.send(b"OK")
            fs=""
        for file in files:
            if file[0]!="." and os.path.isfile(self.path+file):
                fs+=file+"\n"
            self.connfd.send(fs.encode())
        self.connfd.send(b"##")
    def do_get(self,filename):
        self.filename =filename
        try:
            uPath = self.path+self.filename
            print(uPath)
            self.f01 = open(uPath,"rb",-1)
        except Exception:
            self.connfd.send("未找到此文件".encode())
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        while True:
            date = self.f01.read(1024)
            if not date:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(date)
#客户端请求处理函数
def handle(connfd):
    cls = connfd.recv(1024).decode()
    Path = Filepath+ cls+"\\"
    print(Path)
    ftp=FtpServer(connfd,Path)
    while True:
        date = connfd.recv(1024).decode()
        if not date or date[0]=="Q":
            print("结束进程，上一空行为结束消息")
            return
        elif date[0]=="L":
            ftp.do_list()
        elif date[0]=="F":
            filename = date.split(" ")[-1]
            ftp.do_get(filename)


#网络搭建
def main():
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(3)
    print("listen the port 8888....")
#多客户端
    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            print("exit the server")
            return
        except Exception as e:
            print(e)
            continue
        print("connect the client:",addr)
        #创建多线程
        client = Thread(target= handle, args =(connfd,))
        client.setDaemon(True)
        client.start()
        client.join()
if __name__ =="__main__":
    main()