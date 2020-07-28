from socket import *
import struct
ADDR=("192.168.93.1",8888)
st =struct.Struct("i32sif")
s= socket(AF_INET,SOCK_DGRAM)
while True:
    print("=============================")
    id = int(input("ID:"))
    name =input("name:").encode()
    age= int(input("age:"))
    score =float(input("score:"))
    date =st.pack(id,name,age,score)

    s.sendto(date,ADDR)

s.close()