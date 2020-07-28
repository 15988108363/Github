from socket import *
from select import *
#设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)
#创建poll对象
p01 = poll()
#建立查找字典{fileno：io_odj}
fdmap = {s.fileno():s}
#设置关注IO
p01.register(s,POLLIN|POLLERR)
#循环监控io事件发生
while True:
    events = p01.poll()#阻塞等待io发生
    #遍历列表处理IO
    for fd,event in events:
        if fd ==s.fileno():
            c,addr = fdmap[fd].accept()
            print("connect from:",addr)
            p01.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c
        # elif event & POLLHUP:
        #     print("client quited")
        #     p.unregister(fd)#取消关注
        #     fdmap[fd].close()
        #     del fdmap[fd]#从字典删除
        elif event &POLLIN:#客户端发消息
            date= fdmap[fd].recv(1024)
            #断开发生时date得到空此时POLLIN也会就绪
            if not date:
                p01.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(date.decode())
            fdmap[fd].send(b"OK")





