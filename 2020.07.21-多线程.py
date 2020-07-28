from threading import Thread
from time import sleep
#含有参数的线程函数
def fun(sec,name):
    print("线程函数传参：")
    sleep(sec)
    print("%s 线程执行完毕"%name)
def func():
    sleep(3)
    print("线程属性：")
#创建多线程
jobs=[]
for i in range(15):
    t = Thread(target=fun,args=(2,),kwargs={"name": "T%d" % i})
    t.start()
for i in jobs:
    i.join()

t=Thread(target=func,name="asdfgh")
print("Thread name:",t.getName())
t.setName("qwertyu")
print("Thread name:",t.getName())
print("is_alive:",t.is_alive())