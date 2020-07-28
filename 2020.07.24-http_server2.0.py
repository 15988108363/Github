"""http server v2.0
IO 并发处理
基本的request解析
使用类封装
"""
from socket import *
from select import select
#将具体的http server功能封装
class HTTPServer:
    def __init__(self,server_address,static_dir):
        #添加属性
        self.server_addr = server_address
        self.static_dir = static_dir
        self.create_socket()
        self.rlist = self.wlist =self.xlist = []
        self.bind()
    #创建套接字
    def create_socket(self,level=SOL_SOCKET,optname=SO_REUSEADDR, value=-1):
        self.sockfd = socket()
        self.sockfd.setsockopt(level,optname,value)
    #绑定地址
    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    def serve_forever(self):
        self.sockfd.listen(5)#监听队列大小可写成属性
        print("Listen the port:%d"%self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr = r.accept()
                    print("Connect from:",addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)
    #处理客户端请求
    def handle(self,connfd):
        #接收http请求
        requset = connfd.recv(4096)
        print(requset)
        if not requset:
            self.rlist.remove(connfd)
            connfd.close()
            return
        #请求解析
        requset_line = requset.splitlines()[0]
        info = requset_line.decode().split(" ")[1]
        print(connfd.getpeername(),":",info)
        #info分为访问网页和其他
        if info == "/"  or info[-5:] == ".html":
            self.get_html(connfd,info)
        else:
            self.get_date(connfd,info)
        self.rlist.remove(connfd)
        connfd.close()
    def get_html(self,connfd,info):
        #网页文件
        if info == "/":
            filename = self.static_dir + "\index.html"
            print(filename)
        else:
            filename = self.static_dir + info
            print(filename)
        try:
            fd = open(filename,"r",encoding='utf-8')
        except Exception:
            #没有网页
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody ="<h1>Soor,Not found the page</h1>"
        else:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "\r\n"
            responseBody=fd.read()
            print("测试行77")
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())
    #其他情况暂不做处理
    def get_date(self,connfd,info):
        responseHeaders = "HTTP/1.1 200 OK\r\n"
        responseHeaders += "\r\n"
        responseBody ="<h1>Waiting httpserver 3.0</h1>"
        print("测试行88")
        response = responseHeaders + responseBody
        connfd.send(response.encode())
#如何使用HTTPServer类
if __name__ == '__main__':
    #用户自己决定：地址内容
    server_addr=("0.0.0.0",8888)#服务器地址
    static_dir = "E:\python_exercise_http\http_server\Html"#网页存放地址

    httpd = HTTPServer(server_addr,static_dir)#生成实例对象
    httpd.serve_forever()#启动服务
