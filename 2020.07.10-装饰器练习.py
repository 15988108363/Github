def adc(func):
    def wrapper(*args,**kwargs):
        if func.__name__ =="enter_background":
            print(func.__doc__)
            print("许可进入后台....")
            return func(*args,**kwargs)
        elif func.__name__ == "delete_order":
            print("删除订单")
            return func(*args,**kwargs)
    return wrapper

@adc
def enter_background(loginId,pwd):
    print(loginId,pwd)
    print("进入后台系统。。。")
@adc
def delete_order(order_id):
    print("删除订单%d。。。"%order_id)
dict01={2016339910036:123456,"qwe":123}
enter_background(2016339910036,123456)
delete_order(12212)
#===========================================
def Verify_account(func):
    def wrapper(*args,**kwargs):
        if money <=10000:
            return func(*args,**kwargs)
    return wrapper

@Verify_account
def deposit(money):
    print("存款：",money)
def withdraw():
    print("取钱")
    return 10000
deposit(5000)
print(withdraw())