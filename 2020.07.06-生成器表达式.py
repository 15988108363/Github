list01 = [1,2,3,4,5,6,7,8,9]
result01 = [item**2 for item in list01]#列表推导式 字典推导式{键：值 for。。。} 集合{for...}
print(result01)
result02 = (item**2 for item in list01)#生成表达式
print(result02)
for i in result02:
    print(i,end=" ")
print("\t")
result03 = [item for item in list01 if item >3]#本行代码：执行所有结果
result04 = (item for item in list01 if item >3)#本行代码：返回生成器
print(result03)
print(result04)
for i in result04:
    print(i,end=" ")
print("\t")