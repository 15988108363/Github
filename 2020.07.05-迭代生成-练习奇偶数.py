def get_even(target):
        for item in target:
            if item % 2 ==0:
                set02.add(item)
                yield item

def output_even(iterator_obj,list_obj):#取偶数方式1
    for i in range(len(list_obj)):
        i +=1
        try:
            iterator_obj.__next__()
        except:
            break

list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list02 = []
set02 =set()
number = 0
target01 = get_even(list01)#取偶数方式2
for i in target01:
    print(i)
    list02.append(i)
output_even(target01,list01)
print(set02)
print(list02)
print("="*40)
#==================练习2================================
class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
    def __str__(self):
        return "%s--%s--%d--%d"%(self.name,self.sex,self.age,self.score)

def pick_female(target):
    for item in target:
        if item.sex == "女":
            yield (item.name,item.sex,item.age,item.score)

list_stu = [Student("张无忌","男",28,100),
            Student("赵敏","女",25,89),
            Student("周芷若","女",26,88)
            ]
list02 = []
iter01 = pick_female(list_stu)
for i in iter01:
    print(i)
    list02.append(i)
print(list02)
for i in list02:
    print(type(i),end=" ")
    print("\t")
    for k in i:
        print(type(k),end=" ")