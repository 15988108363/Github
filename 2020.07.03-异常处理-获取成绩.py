def get_score():
    score  = int(input("请输入成绩："))
    print(score)

def score_judge():
    pass_number = 1
    while pass_number ==1:
        try:
            get_score()
        except ValueError as v:
            print(v)
            print("输入值有误")
            continue
        except TypeError as t:
            print(t)
            print("输入值类型有误")
            continue
        except NameError as n:
            print(n)
            print("位置类型错误")
            continue
        except Exception as e:
            print(e)
            print("位置类型错误")
            continue
        else:
            pass_number = 0

def judge():
    while True:
        try:
            number = int(input("请输入成绩："))
        except:
            print("输入有误")
            continue
        if 1<= number <=100:
            return number
        print("成绩不在范围内")

judge()
get_score()
score_judge()
