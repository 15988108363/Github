from socket import *
import sys
ADDR = ("192.168.93.1",8888)
Filetemp = r"""D:\PyCharm——练习文件\临时文件\temp"""
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b"L")#发送请求
        date =self.sockfd.recv(128).decode()
        if date=="OK":
           while True:
               date=self.sockfd.recv(128)
               if date==b"##":
                   break
               print(date.decode())
        else:
            print(date)
    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit("Tanks for your using")
    def get_file(self,filename):
        self.sockfd.send(("F "+filename).encode())
        date = self.sockfd.recv(128).decode()
        if date=="OK":
            fd =open(Filetemp,"wb")
            while True:
                date=self.sockfd.recv(1024)
                if date == b"##":
                    break
                fd.write(date)
def request(sockfd):
    ftp = FtpClient(sockfd)
    while True:
        print("\n=============option================")
        print("****************list*****************")
        print("*****************get file************")
        print("*******************quit**************")
        print("=====================================")
        cmd = input("please input your commond:")
        if cmd.strip() =="list":
            ftp.do_list()
        elif cmd[:3] =="get":
            filename = cmd.split(" ")[-1]
            ftp.get_file(filename)
        elif cmd.strip() =="quit":
            ftp.do_quit()
        else:
            print("wrong input,return")
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("connect failed")
    else:
        print("""****************\nDate File Image\n****************""")
        cls = input("please file type:")
        while cls not in ("Date","File","Image"):
            print("The type not found")
            cls = input("please file type again:")
        sockfd.send(cls.encode())
        request(sockfd)
        date =sockfd.recv(1024)
        print("from server",date)
        sockfd.close()
if __name__ =="__main__":
    main()
