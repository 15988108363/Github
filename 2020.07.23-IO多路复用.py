"""select 函数讲解"""
from socket import *
from select import select
#做进IO作用监听套接字
s =socket()
s.bind(("0.0.0.0",8888))
s.listen(3)
fd =open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","r+")
while True:
    date = fd.readline()
    print("读取到的内容：", date)
    if not date:
        break
print("开始提交监控的IO")
rs,ws,xs = select([s],[fd],[])
print("rs:",rs)
print("ws:",ws)
print("xs:",xs)