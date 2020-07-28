"""http功能演示
将网页发送给浏览器展示"""

from socket import *

def handle(connfd):
    print("request from:",connfd.getpeername())
    request = connfd.recv(4096)#接收http请求
    #将request进行行分割
    request_line =request.splitlines()[0].decode()
    #获取请求内容
    info=request_line.split(" ")[1]
    if info=="/":
        f=open("index.html")
        response="HTTP/1.1 200 ok\r\n"
        response += "Context-Type:text/html\r\n"
        response += "\r\n"
        response +=f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Context-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>sorry..<h1>"
    connfd.send(response.encode())
    print(request.decode())
    print(request_line.decode())
#搭建tcp网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8888))
    sockfd.listen(3)
    print("listen the port 8888...")
    while True:
        connfd,addr = sockfd.accept()
        handle(connfd)#处理浏览器请求
if __name__ == '__main__':
    main()
