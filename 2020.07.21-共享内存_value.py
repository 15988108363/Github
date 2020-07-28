from multiprocessing import Process,Value,freeze_support
import time
import random
#操作共享内存
def man(money):
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1,1000)
def girl(money):
    for i in range(30):
        time.sleep(0.5)
        money.value -= random.randint(100,900)

if __name__ =="__main__":
    freeze_support()
     # 创建共享内存
    money =Value("i",5000)
    m01 =Process(target=man,args=(money,))
    m02 =Process(target=girl,args=(money,))
    m01.start()
    m02.start()
    m01.join()
    m02.join()
    #获取共享内存值
    print("月余额：",money.value)