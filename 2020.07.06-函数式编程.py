"""
    lambda表达式
    lambda 参数 :方法体
"""
def fun01():
    print("我是普通方法")
a01 = lambda :print("我是lamba方法")
a01()
def fun02(a):
    print("我是普通方法,参数是：",a)

fun02(500)
def fun03():
    return True
print(fun03())
a02 = lambda a:print("我是普通方法,参数是：",a)
a02(500)
a04 =lambda :True
print(a04())
#-----------------------------------------------
list01 = [1,23,4,12,12,121,332,212,12111]
def fn01():
    for item in list01:
        if item>=5:
            yield item
result01 = fn01()
print(result01)
print(result01.__next__())
print(id(result01))
print(id(result01.__next__()))
print(id(result01.__next__()))
print(dir(result01))
#===============================================
def find_demo(target,assumpt_condition):
    max_number =target[0]
    for item in range(1,len(target)-1):
        if assumpt_condition:
            max_number =target[item+1]
    print(max_number)

f01 = find_demo(list01,lambda item:target[item]<target[item+1])