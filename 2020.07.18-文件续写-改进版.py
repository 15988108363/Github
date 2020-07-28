import time
import os
f01 =open("D:\\PyCharm——练习文件\\临时文件\\2020.07.18-改进.txt","a+",-1)
f01.seek(0)
n =1
for line in f01:
    n+=1
while True:
    time.sleep(1)
    s ="%d.  %s\n"%(n,time.ctime())
    f01.write(s)
    f01.flush()
    n +=1
f01.close()