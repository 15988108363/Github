"""文件偏移量"""
fd = open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","w+",1)
fd.write("hello,world\n")
fd.flush()
date = fd.read()
print(date)
print("当前文件偏移量位置：",fd.tell())#相对于开头位置
fd.close()
print("="*40)

fd = open("D:\PyCharm——练习文件\临时文件\第一个文件.txt","a+",1)
print("文件描述符",fd.fileno())
date = fd.read()
print(date)
print("当前文件偏移量位置：",fd.tell())
fd.seek(0)#开头算起
print("当前文件偏移量位置：",fd.tell())
fd.seek(0,2)#末尾算起
print("当前文件偏移量位置：",fd.tell())
fd.seek(0,1)#当前位置算起
print("当前文件偏移量位置：",fd.tell())
fd.close()
print("="*40)