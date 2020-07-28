def get_evev01(target):
    for item in target:
        if item %2 ==0:
            yield item

def get_evev02(target):
    result =[]
    for item in target:
        if item %2 ==0:
            result.append(item)
    return result
def generate_number():
    import random as r
    for i in range(2000):
        i +=1
        number = r.randint(1,10000)
        list01.append(number)
list01 =[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,57,
         34,45,67,1212,121,11,12,32,33,47,353,45,
         343,3434,56,67,78,90,1211,23,321,451,787]
list02 =[]
list03 =[]
generate_number()
iter01 = get_evev01(list01)#没有执行方法体
for item in iter01:#循环（next)一次，计算一次，返回一次
    list02.append(item)
print(list02)
iter01 = get_evev01(list01)#执行方法体，将所有结果存在内存中
for item in iter01:
    list03.append(item)
print(list03)