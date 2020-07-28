"""TCP"""
import socket
sockfd =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)
while True:
    print("connecting....")
    try:
        connfd,addr =sockfd.accept()
        print("connect from:",addr)
    except KeyboardInterrupt:
        print("exit")
        break
while True:
    date = connfd.recv(1024)
    if not date:
        break
    print("receive:",date)
    n =connfd.send(b"Accept")#字节串
    print("send %d bytes"%n)
sockfd.close()