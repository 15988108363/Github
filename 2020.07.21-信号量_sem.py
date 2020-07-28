from multiprocessing import Semaphore,Process
from time import  sleep
import os
def handle(target):
    print("%d 想执行时间"%os.getpid())
    target.acquire()
    print("%d 开始执行时间" % os.getpid())
    sleep(3)
    print("%d 完成时间" % os.getpid())
    target.release()
if __name__=="__main__":
    #创建信号量，最大运行3个进程事件
    sem =Semaphore(3)
    job =[]
    for i in range(10):
        p=Process(target=handle,args=(sem,))
        job.append(p)
        p.start()
    for i in job:
        i.join()
    print(sem.get_value())
