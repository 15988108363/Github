#multiprocessing
import multiprocessing as mp
from time import sleep
a=1
def fun():
    print("子进程开始执行")
    global a
    a=3
    print("child",a)
    sleep(3)
    print("子进程执行完毕")
#创建进程对象
if __name__ =="__main__":
#windows系统下必须写保护代码才能执行mulitiprocesing
#或者写multiprocessing.freeze_support()静态方法
    mp.freeze_support()
    p = mp.Process(target = fun)
#启动进程
    p.start()
    sleep(2)
    print("parent",a)
#回收进程
    p.join()