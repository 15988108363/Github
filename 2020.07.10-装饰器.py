def print_func_name(func):
    #包装旧功能
    def wrapper(*args,**kwargs):
        #增加新功能
        print(func.__name__)
        print("hihi")
        #旧功能
        return func(*args,**kwargs)
    return wrapper #返回包装器

@print_func_name
def say_hello(age,name):
    print("hello",name,age)
    return "hh"
say_hello(25,"张无忌")