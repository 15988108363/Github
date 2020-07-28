"""进程池原理"""
from multiprocessing import Pool,freeze_support
from time import sleep,ctime
#进程池事件
def worker(msg):
    sleep(2)
    print(msg)
if __name__ =="__main__":
    freeze_support()
    #创建进程池
    pool = Pool(4)
    #添加事件
    for i in range(20):
        msg = "Hello %d"%i
        p=pool.apply_async(func= worker,args=(msg,))
        print(p)
    #关闭进程池
    pool.close()
    #回收进程池
    pool.join()

    print(p.get)