"""

"""
list01 = ["a","b","c","d","e"]
for item in enumerate(list01):  # 索引，元素
    print(item)
    print(type(item))
for index,element in enumerate(list01):
    print(index,element)
#============================================
def enumerate01(target_list):
    index= 0
    for item in target_list:
        yield (index,item)
        index +=1
list02 = ["d","e","f","g"]
for item in enumerate(list01):  # 索引，元素
    print(item)
    print(type(item))
for index,element in enumerate01(list01):
    print(index,element)
for item in zip(list01,list02):
    print(item)
print("="*40)
#==============================================
def my_zip(*args):
    list03 =(args[number02][number01] for number01 in range(len(args)) for number02 in range(len(args)))#生成器表达式
    yield tuple(list03)
list03 = [1,2,3,4,5,6,7,8,9]
for item in zip(list01,list02,list03):
    print(item)
