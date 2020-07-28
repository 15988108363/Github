from multiprocessing import Process,freeze_support
import os
def top(size):
    target = open(r"D:\PyCharm——练习文件\临时文件\20171002_143707.jpg", "rb", -1)
    n = size//2
    fw= open(r"D:\PyCharm——练习文件\临时文件\2020.07.21_temp01.jpg","wb")
    fw.write(target.read(n))
    target.close()
    fw.close()

def bottom(size):
    target = open(r"D:\PyCharm——练习文件\临时文件\20171002_143707.jpg", "rb", -1)
    target.seek(size//2,0)
    fw= open(r"D:\PyCharm——练习文件\临时文件\2020.07.21_temp02.jpg","wb")
    while True:
        date = target.read(1024)
        if not date:
            break
        fw.write(date)
    target.close()
    fw.close()
if __name__ =="__main__":
    #父进程打开文件，文件偏移量会互相影响
    size = os.path.getsize(r"D:\PyCharm——练习文件\临时文件\20171002_143707.jpg")
    print(size)
    t01 = Process(target=top,args=(size,))
    t02 = Process(target=bottom, args=(size,))
    t01.start()
    t02.start()
    t01.join()
    t02.join()