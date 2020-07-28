from socket import *
import os
if __name__ =="__main__":
    socket_file ="./sock"
    if os.path.exists(socket_file):
        os.remove(socket_file)
    sockfd = socket(AF_UNIX,SOCK_STREAM)
    sockfd.bind(socket_file)
    while True:
        msg =input(">>")
        if not msg:
            break
        sockfd.send(msg.encode())
    sockfd.close()