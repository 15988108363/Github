from multiprocessing import Process,Array,freeze_support
import time
import random
def fun(target):
    for i in target:
        print(i,end=' ')
    print(target.value)
if __name__=="__main__":
    freeze_support()
    #创建共享内存
    #共享内存开辟5个整型列表空间
    shm = Array("c",b"hello")
    p = Process(target=fun,args=(shm,))
    p.start()
    p.join()


