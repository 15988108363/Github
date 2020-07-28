import threading
from time import sleep
import os
def music():
    global a
    for i in range(5):
        sleep(2)
        a +=1
        print(os.getpid(),"peaceful")
a =1
t = threading.Thread(target=music)
t.start()#分支线程
for i in range(3):
    sleep(3)
    print(os.getpid(),"sounds good")
t.join()
print("main thread a:",a)