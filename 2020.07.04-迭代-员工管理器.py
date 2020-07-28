class Salary_calculator:
    salary_list = []
    def __init__(self,name,position,basic_salary=0,extra_wages=0,target=""):
        self.name = name
        self.position = position
        self.basic_salary = basic_salary
        self.extra_wages = extra_wages
        self.index = 0
        self.target = target
        self.record_salary()
    def __repr__(self):
        return '("%s","%s",%d,%d)'%(self.name,self.position,self.basic_salary,self.extra_wages)
    def __iter__(self):
        pass
    def total_wages(self):#个人总工资
        self.total_wages = self.basic_salary + self.extra_wages
        print("%s%s总工资为：%d"%(self.position,self.name,self.total_wages))
    def record_salary(self):#将工资放入容器
        item = eval(self.__repr__())              #字符串转变成元组
        Salary_calculator.salary_list.append(item)#将元组插入列表，而不是对象
    def required_money(self):#公司所需总金额
        pass
    def __next__(self):
        #返回下一个元素
        #如果索引越界 则抛出异常
        if self.index > len(self.target)-1:
            raise StopIteration()
        #返回下一个元素
        item = self.target[self.index]
        self.index +=1
        return item

#=================创建职位============================
class General_staff(Salary_calculator):
    pass
class Saleman(Salary_calculator):
    pass
class Programer(Salary_calculator):
    pass
# =================创建员工============================
s01 =Salary_calculator("张三","会计",1000,4500)
g01 = General_staff("李四","普通员工",2000,5000)
s02 =Saleman("王二","销售员",3000,6000)
p01 =Programer("牛大","编程员",5000,8000)
S01 =Salary_calculator("熊熊","老板").required_money()
print(Salary_calculator.salary_list)
#==================迭代器==============================
list01 = ([Salary_calculator("张三","会计",1000,4500),General_staff("李四","普通员工",2000,5000),Saleman("王二","销售员",3000,6000)])
for item in list01:
    print(item)

for item in Salary_calculator.salary_list:
    for i in item:
        print(i,end =" ")
        print(type(i))
for item in list01:
    item.__iter__()
    item.__next__()

