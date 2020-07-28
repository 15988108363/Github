from multiprocessing import Process,freeze_support
from time import sleep
import os

def th1():
    sleep(3)
    print("eating..")
    print(os.getppid(),"....",os.getpid())
def th2():
    sleep(2)
    print("sleep..")
    print(os.getppid(),"....",os.getpid())
def th3():
    sleep(4)
    print("hit doudou..")
    print(os.getppid(),"....",os.getpid())
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print(" I‘m %s"%name)
        print("I'm working....")
if __name__ =="__main__":
    freeze_support()
    things=[th1,th2,th3]
    jobs =[]
    for th in things:
        p = Process(target= th)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
    p = Process(target=worker,args=(2,"asd"))
    p.daemon=True
    p.start()
    print(dir(p))
    print(p.__dict__)
    print(p.name)
    print(p.pid)
    print(p.is_alive())
    sleep(4)


