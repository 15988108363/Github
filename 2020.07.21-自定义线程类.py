from threading import Thread
class Thread01(Thread):
    def __init__(self,attr):
        self.attr = attr
        super().__init__()
    def f1(self):
        print("步骤一：")
    def f2(self):
        print("步骤2：")
    def run(self):
        self.f1()
        self.f2()

t = Thread01("assas")
t.start()
t.join()
