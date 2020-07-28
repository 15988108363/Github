import time
def print_time(func):
        def calculate_time(*args, **kwargs):
            t01 = time.time()
            result = func(*args,**kwargs)
            t02 = time.time() - t01
            print(t02)
            return result
        return calculate_time
class student:
    def __init__(self,name):
        self.name= name
    @print_time
    def study(self):
        print("开始学习啦")
        time.sleep(2.0)

s01 = student("ass")
s01.study()
