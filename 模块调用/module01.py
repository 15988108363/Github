__all__ = ["fun01","MyClass01","fun04"]#可以导出的函数
__doc__ = ["这是module01模块"]
print("我是module01")
def fun01():
    print("fun01")
class MyClass01:
    def fun02(self):
        print("fun02")

def _fun03():
    print("fun03")
def fun04():
    print("fun04")