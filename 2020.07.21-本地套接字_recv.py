from socket import *
import os
if __name__ =="__main__":
    socket_file ="./sock"
    if os.path.exists(socket_file):
        os.remove(socket_file)
    sockfd = socket(AF_UNIX,SOCK_STREAM)
    sockfd.bind(socket_file)
    sockfd.listen(3)
    while True:
        c,addr=sockfd.accept()
        while True:
            date = c.recv(1024)
            if not date:
                break
            print(date.decode())
        c.close()
    sockfd.close()

