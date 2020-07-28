from threading import Thread,RLock
import time
num =0
lock =RLock()#在一个线程内可重复上锁
class MyThread(Thread):
    def fun1(self):
        global num
        with lock:
            num -=2
    def fun2(self):
        global num
        if lock.acquire():
            num +=1
            if num>5:
                self.fun1()
            print("num:",num)
            lock.release()
    def run(self):
        while True:
            time.sleep(2)
            self.fun2()
for i in range(10):
    t=MyThread()
    t.start()
