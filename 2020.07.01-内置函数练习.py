class Student:
    def __init__(self,name,age,score):
        self.name,self.age,self.score = name,age,score
    def __repr__(self):
        return "Hello World"
    def infos(self):
        m = "Hello China"
        print(m)
    def __str__(self):
        return self.infos()

s1 = Student("Woq",23,44)
print(s1.__dict__)

