class Salary_calculator:
    salary_list = []
    def __init__(self,name,position,basic_salary=0,extra_wages=0):
        self.name = name
        self.position = position
        self.basic_salary = basic_salary
        self.extra_wages = extra_wages
        self.record_salary()
    def total_wages(self):#个人总工资
        self.total_wages = self.basic_salary + self.extra_wages
        print("%s%s总工资为：%d"%(self.position,self.name,self.total_wages))
    def record_salary(self):#将工资放入容器
        record_dict = {}
        record_dict["姓名"] = self.name
        record_dict["员工职位"] = self.position
        record_dict["底薪"] = self.basic_salary
        record_dict["额外工资"] = self.extra_wages
        Salary_calculator.salary_list.append(record_dict)
    def required_money(self):#公司所需总金额
        self.company_required_money = 0
        for dict in Salary_calculator.salary_list:
             dict01 = dict["底薪"]+dict["额外工资"]
             self.company_required_money += dict01
        print("%s%s要发的工资所需：%d"%(self.position,self.name,self.company_required_money))
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
p01 =Programer("牛大","编程员",5000,8000)
S01 =Salary_calculator("熊熊","老板").required_money()