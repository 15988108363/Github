from socket import *
from select import select
#设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)
#设置关注的IO
rlist = [s]
wlist = []
xlist = []
#监控IO的发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历三个返回值列表,判断哪个IO发生
    for r in rs:
        #如果是套接字就绪就处理连接
        if r is s:
            c,addr = r.accept()
            print("Connect from:",addr)
            rlist.append(c)#加入新的关注IO
        else:
            date = r.recv(1024).decode()
            if not date:
                rlist.remove(r)
                r.close()
                continue
            print(date)
            #r.send(b"OK")
            #我们希望主动处理这个IO
            wlist.append(r)
    for w in ws:
        w.send(b"OK Thanks")
        wlist.remove(w)
    for r in rs:
        pass