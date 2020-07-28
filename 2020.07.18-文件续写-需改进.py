import time
import os
class file_input:
    def __init__(self,year=2020,month=7,day=18,hour=0,minute=0,second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    def open_file(self):
        if not os.path.exists("D:\\PyCharm——练习文件\\临时文件\\2020.07.18.txt"):
            self.p01 =open("D:\\PyCharm——练习文件\\临时文件\\2020.07.18","w",-1)
        else:
            self.p01= open("D:\\PyCharm——练习文件\\临时文件\\2020.07.18.txt","a+",-1)
    def input(self,number=1):
        while self.minute <= number:
            time.sleep(1)
            self.second +=1
            if self.second ==60:
                self.second =0
                self.minute +=1
            if self.minute ==60:
                self.minute =0
                self.hour +=1
            if self.hour ==24:
                self.hour =0
                self.day +=1
            if self.day ==30:
                self.day = 1
                self.month +=1
            if self.month ==13:
                self.month = 1
                self.year +=1
            self.p01.write("%d-%02d-%02d-%02d-%02d-%02d\n"%(self.year,self.month,self.day,self.hour,self.minute,self.second))
            print("%d-%02d-%02d-%02d-%02d-%02d\n"%(self.year,self.month,self.day,self.hour,self.minute,self.second))
            self.p01.flush()
    def is_empty(self):
        if os.path.getsize("D:\\PyCharm——练习文件\\临时文件\\2020.07.18.txt") >0:
            return False
        return True
    def continue_input(self,number=2):
        self.number =number
        if self.is_empty():
            self.input()
        else:
            print(self.p01.seek(0,2))
            self.input(self.number)
    def close_file(self):
        return  self.p01.close()

f01 = file_input()
f01.open_file()
f01.input()
f01.continue_input()
f01.close_file()
f01.open_file()
f01.input()
f01.continue_input()
f01.close_file()