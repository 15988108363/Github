def fun01():
    print("fun01执行了")
    a=1
    def fun02():
        print("fun02执行了")
        print("外部变量是：",a)
    return fun02

result01 = fun01()
#调用内部函数，因为内部函数使用了外部函数，所以称为闭包
result01()#可以使用外部变量，说明外部变量在调用后没有释放
def give_money(money):
    def child_buy(target,price):
        nonlocal money
        if money >= price:
            money -=price
            print("孩子花了%d钱，买了%s，还剩%d"%(price,target,money))
        else:
            print("压岁钱不足")
    return child_buy

result02 = give_money(1200)
result02("飞机",122)
result02("坦克",980)
'''装饰器'''
def say_hello():
    print("hello")
    print(say_hello.__name__)
say_hello()
def print_funv_name(func):
    print(func.__name__)
print_funv_name(say_hello)
print("="*20)
#================================
def print_fun_name02(func):
    def wrapper():
        #增加新功能
        print(func.__name__)
        #旧功能
        #func
    return wrapper#返回包装器
say = print_fun_name02(say_hello)
say()
#缺点：调用者完成包装新旧方法的任务
#解决：应有定义者完成