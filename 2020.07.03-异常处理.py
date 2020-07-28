def div_apple(apple_count):
    person_count = int(input("请输入人数："))#ValueError
    result = apple_count / person_count
    print("每个人分%d个苹果"%result)

#不能根据具体错误，做出相应逻辑处理
#try:
#   div_apple(12)
#except Exception as e:#捕获所有类型的异常
## print("qwqw")
# print(">>>>>>>后续逻辑")


try:
    div_apple(12)
except ValueError as v:#捕获ValueError类型异常
    print(v.args)
    print("输入人数有误")
except ZeroDivisionError:#捕获该类型异常
    print("人数不能是零")
except Exception as e:#捕获所有类型异常
    print("未知类型错误")
else:#没有发生异常，执行的逻辑
    print("分苹果成功了")
finally:
    print("无论是否发生异常都会执行的逻辑")

print(">>>>>>>后续逻辑")