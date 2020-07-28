"""管道通信"""
from multiprocessing import Process,Pipe,freeze_support
import os,time
#创建管道
def fun(name,fd2):
    time.sleep(2)
    #向管道写入内容
    fd2.send({name:os.getpid()})

if __name__ == "__main__":
    freeze_support()
    # 创建管道
    fd1,fd2 = Pipe(False)
    jobs = []
    for i in range(5):
        p = Process(target=fun,args=(i,fd2))
        jobs.append(p)
        p.start()

    for i in range(5):
        date = fd1.recv()
        print(date)

    for p in jobs:
        p.join()