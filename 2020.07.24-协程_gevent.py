import gevent
import time
from gevent import monkey
def foo(a,b):
    print("runing foo...",a,b)
    gevent.sleep(2)
    print("foo again")

def bar():
    print("running bar ....")
    gevent.sleep(3)
    print("bar again")

#将函数封装成为协程，遇到gevent阻塞自动执行
f = gevent.spawn(foo,1,"hello")
g = gevent.spawn(bar)

gevent.joinall([f,g])#等待f，g结束