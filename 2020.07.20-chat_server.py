"""Chat room
env:python3.8
socket fork
"""
from socket import *
import os,sys
#global variable
ADDR=("0.0.0.0",8888)
user ={}
def do_login(s,name,addr):
        if name in user or "superviser" in name:
            s.sendto("the user alreadly have".encode(),addr)
            return
        s.sendto(b"ok",addr)
        msg ="welcome to room"%name
        for i in user:
            s.sendto(msg.encode(),user[i])
        user[name]= addr
def do_chat(s,name,text):
    msg ="%s : %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),usr[i])
def do_quit(s,name):
    msg = "%s exit the room"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),usr[i])
        else:
            s.sendto(b"EXIT",user[i])
    del user[name]

def do_request(s):
    while True:
        date, addr = s.recvfrom(1024)
        print("server received:", date.decode(), addr)
        msg =date.decode().split(" ")
        if msg[0]== "L":
            do_login(s,msg[1],addr)
        elif msg[0]=="C":
            text = " ".join(msg[2:])
            do_chat(s,msg[1],text)
        elif msg[0]== "Q":
            if msg[1] not in user:
                s.sendto(b"EXIT",addr)
                continue
            do_quit(s,msg[1])

#create net connect
def main():
    s= socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid <0:
        return
    elif pid ==0:
        while True:
            msg = input("superviser message")
            msg = "C superviser message"+msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)
if __name__ =="__main__":
    main()