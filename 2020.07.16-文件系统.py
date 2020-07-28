import time
fd = open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","w",-1)
fd.write("qqwwe")
fd.close()
fd01=open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","a",-1)
fd01.write("qqwwe")
fd01.close()
fd02=open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","w+",-1)
fd02.write("qqwweqwwqw\nqwwwwqds\n")
fd02.write("qqwweqwwqw\nqwwwws")
fd02.close()
fd03=open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","r",-1)
date = fd03.read(5)
print("读取到的内容：",date)
while True:
    time.sleep(1)
    date = fd03.read(8)
    print("读取到的内容：", date)
    if not date:
        break
fd03.close()
fd04=open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","r",-1)
while True:
    time.sleep(1)
    date01 = fd04.readline()
    print("读取到的内容：", date01)
    if not date:
        break
while True:
    time.sleep(1)
    date02 = fd04.readlines()
    print("读取到的内容：", date02)
    if not date:
        break
fd04.close()
fd05=open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","r",-1)
for i in fd05:
    print(i)
fd05.close()
fd06=open("D:\PyCharm——练习文件\临时文件\第一个文件","a",-1)
fd06.writelines(["qwertyuiopmnhgfds\n","qasdfghjk\n"])
fd06.close()