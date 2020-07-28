from socket import *
#创建tcp套接字
s = socket()
s.bind(("192.168.61.1",8888))
s.listen(3)
c,addr = s.accept()
print("connect from:",addr)
date = c.recv(4096)
print(date)
date = """HTTP/1.1 200 ok
Content_Type:text/html

<h1>hello world</h1>
"""
c.send(date.encode())
c.close()
s.close()