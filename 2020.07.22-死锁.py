import time
import threading
class Account:
    def __init__(self,_id,balance,lock):
        self.id=_id
        self.balance = balance
        self.lock = lock
    def withdraw(self,amount):
        self.balance -=amount
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance
def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount)
        time.sleep(0.5)
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        from_.lock.release()
    print("completed")

a01= Account("abby",8000,threading.Lock())
a02 = Account("levi",10000,threading.Lock())
t01=threading.Thread(target=transfer,args=(a01,a02,1500))
t02=threading.Thread(target=transfer,args=(a02,a01,500))
t01.start()
time.sleep(9)#处理死锁
t02.start()
t01.join()
t02.join()
print("a01:",a01.get_balance())
print("a02:",a02.get_balance())