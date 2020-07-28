from socket import *
import os,sys
#server address
ADDR =("192.168.93.1",8888)

def send_msg(s,name):
    while True:
        try:
            text = input("input:")
        except KeyboardInterrupt:
            text ="quit"
        if text =="quit":
            msg = "Q "+ name
            s.sendto((msg.encode(),ADDR))
            sys.exit("exit room")

        mag = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)
def recv_meg(s):
    while True:
        date,addr =s.recvfrom(2048)
        if date.decode()=="EXIT":
            sys.exit()
        print(date.decode()+"\n speak:",end=" ")
def main():
    s =socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("name:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        date,addr = s.recvfrom(1024)
        if date.decode()=="ok":
            print("enter the room")
            break
        else:
            print(date.decode())
#create new process
    pid =os.fork()
    if pid <0:
        sys.exit("error")
    elif pid ==0:
        send_msg(s,name)
    else:
        recv_msg(s)
if __name__ =="__main__":
    main()