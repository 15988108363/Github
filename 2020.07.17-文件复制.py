filename = input(("Filename:"))#文件名称
filenamev="D:\\PyCharm——练习文件\\临时文件\\"+ filename
try:
    fr = open(filenamev,'rb',-1)
except FileNotFoundError as e:
    print(e)
else:
    fw = open(r"D:\PyCharm——练习文件\临时文件\2020.07.17-文件创建","wb",-1)
    #循环读取文件内容
    while True:
        date = fr.read(1024)
        #读到文件结尾
        if not date:
            break
        fw.write(date)
    fr.close()
    fw.close()
