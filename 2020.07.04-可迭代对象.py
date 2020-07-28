"""可迭代对象"""
list01 = [0,1,2,3,4,5,6,7,8,9]
for item in list01:
    print(item,end=" ")
print("\t")
print("="*40)
#=============For 循环原理====================
#1.
iterator = list01.__iter__()
#2.
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
item = iterator.__next__()
print(item,end=" ")
#3.
#item = iterator.__next__()#StopIteration
print("\t")
print("="*40)
#》》》》》》》》》For 循环原理 》》》》》》》》》》》》》
list02 = [0,1,2,3,4,5,6,7,8,9]
iterator = list02.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item, end=" ")
    except StopIteration:
        print("迭代完毕")
        break
#++++++++++++++++++++练习+++++++++++++++++++++++++
print("="*40)
tuple01 = ("悟空","八戒","沙僧","唐僧")
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item, end=" ")
    except StopIteration:
        break
#=====================练习=========================
print("\t")
print("="*40)
dict01 = {"张三丰":101,"张无忌":102,"赵敏":102}
iterator = dict01.__iter__()
item = iterator.__next__()
print(item, dict01[item],end=" ")
item = iterator.__next__()
print(item, dict01[item],end=" ")
item = iterator.__next__()
print(item, dict01[item],end=" ")
