list01 = [1,2,3,45,6,7,8,9]
list02 = [21,23,43,45,65,76]
def fun01(item):
        return item*2
print(list(map(fun01,list02)))
# for item in iter:
#    yield function(item)
def fun02(item):
    return item >3
print(list(filter(fun02,list01)))
# for item in iter:
#    yield function(item)判断True/False return True
list03 = [12,31,1,23,3453,54,23]
print(sorted(list03,key=lambda x:x*2,reverse=False))
# key = function条件
#===================选择排序====================
#if reverse ==False:升序
#    for i in range(len(list03)-1):外层循环控制比较轮数
#     for k in range(i+1,len(list03)):内层循环控制比较次数
#         if key(list03[i]) > key(list03[k]):
#             list03[i],list03[k] = list03[k],list03[i]
#else：降序
#    for i in range(0,len(list03)):
#     for k in range(i+1,len(list03)):
#         if key(list03[i]) < key(list03[k]):
#             list03[i],list03[k] = list03[k],list03[i]
#===================冒泡排序====================
#if reverse ==False:升序
#    for i in range(len(list03)-1):外层循环控制比较轮数
#     for k in range(i+1,len(list03)):内层循环：控制每一轮比较的次数，兼顾参与比较的下标
#         if key(list03[i]) > key(list03[k]):
#             list03[i],list03[k] = list03[k],list03[i]
#else：降序
#    for i in range(len(list03)-1，-i):
#     for k in range(len(list03)-1，-i):
#         if key(list03[i]) < key(list03[k]):
#             list03[i],list03[k] = list03[k],list03[i]
print(max(list03,key=lambda a:a*3))
print(max(list03))