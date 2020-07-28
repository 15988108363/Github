from socket import *
import struct
s=socket(AF_INET,SOCK_DGRAM)
s.bind(("192.168.93.1",8888))
st = struct.Struct("i32sif")
f=open("D:\\PyCharm——练习文件\\临时文件\\student.txt","w")
while True:
    date,addr = s.recvfrom(1024)
    print(date)
    date=st.unpack(date)
    info ="%d %s %d %.2f\n"%(date[0],date[1].decode(),date[2],date[3])
    print(info)
    f.write(info)
    f.flush()
f.close()
s.close()