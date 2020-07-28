class Get_score:
    def __init__(self,score=-1):
        self.score = score

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        while True:
            try:
                value = int(input("请输入成绩："))
            except:
                print("输入有误")
                continue
            if 1 <= value <= 100:
                self.__score = value
                return
            print("成绩不在范围内")


g01 = Get_score()
print(g01.score)