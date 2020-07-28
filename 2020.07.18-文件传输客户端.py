from socket import *
sockfd =socket()
server_addr = ("192.168.93.1",8888)
sockfd.connect(server_addr)
cli01 = open(r"D:\PyCharm——练习文件\临时文件\mmexport1478240319603.jpg","rb",-1)
# for line in cli01:
#     sockfd.send(line)
#     date =sockfd.recv(1024)
while True:
    date =cli01.read(1024)
    if not date:
        break
    sockfd.send(date)
    date = sockfd.recv(1024)
    print("from server",date)
cli01.close()
sockfd.close()