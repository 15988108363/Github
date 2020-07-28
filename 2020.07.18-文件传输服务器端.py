import socket
sockfd =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(1024)
print("connecting....")
connfd,addr = sockfd.accept()
ser01 =open(r"D:\PyCharm——练习文件\临时文件\temp","wb",-1)
while True:
    date = connfd.recv(1024)
    if not date:
        break
    ser01.write(date)
    print("receive:",date)
    n =connfd.send(b"Accepted")#字节串
    print("send %d bytes"%n)
ser01.close()
sockfd.close()