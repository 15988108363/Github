"""缓冲实例"""
fd = open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","w",1)#行缓冲
#0 无缓冲（不允许） 1 行缓冲； n(n>1)名缓冲（此系统不识别）；
while True:
    s = input(">>")
    fd.write(s+"\n")
    fd.flush()#立即刷新缓冲区，将内容传入磁盘
fd.close()