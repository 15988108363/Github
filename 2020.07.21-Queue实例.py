from multiprocessing import Process,Queue,freeze_support
from time import sleep
from random import randint

def request(q):
    for i in range(20):
        x = randint(0,100)
        y = randint(0,100)
        q.put((x,y))
def handle(q):
    while True:
        sleep(0.5)
        try:
            x,y = q.get(timeout = 3)
        except:
            break
        else:
            print("%d + %d = %d"%(x,y,x+y))

if __name__=="__main__":
    freeze_support()
    #创建消息队列
    q01 =Queue(3)
    p1 = Process(target=request,args=(q01,))
    p2 = Process(target=handle, args=(q01,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()