class StudentModel:
    """学生数据模型"""
    def __init__(self, id=0, name="", age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return "编号:%s,姓名:%s,年龄:%d,成绩:%0.2f"%(self.id,self.name,self.age,self.score)
    def __repr__(self):
        return 'StudentModel(%s,%s,%d,%0.2f)'%(self.id,self.name,self.age,self.score)
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @id.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @id.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @id.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:

    def __init__(self, ):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def generate_id(self): # **kwargs
        # 生成编号
        if len(self.__list_stu) > 0:
            id = self.__list_stu[-1].id + 1
        else:
            id = 1
        return id
        #return self.__list_stu[-1].id +1 if len(self.__list_stu)> 0 id=self.__list_stu[-1].id +1 else id=1
    def order_by_score(self):
        new_list = self.__list_stu[:]
        for r in range(len(new_list)-1):
            for c in range(r+1, len(new_list)-1):
                if new_list[r].score > new_list[c].score:
                    new_list[r],new_list[c] = new_list[c],new_list[r]
        return new_list

    def remove_student(self,id):
        """删除学生"""
        for stu in self.list_stu:
            if stu.id == id:
                self.list_stu.remove(stu)
                return True
        return False

class StudentManagerView:
    def __display_menu(self):
        print("1),添加学生")
        print("2),显示学生")
        print("3),删除学生")
        print("4),修改学生")
        print("5),按照成绩降序排列")

    def __select_menu(self):
        number = input("请输入选项")
        if number == 1:
            pass
        if number == 2:
            self.__output_students(self.__manager.list_stu)
        if number == 3:
            self.__delete_student()
        if number == 4:
            self.__modify_student()
        if number == 5:
            self.__output_students_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
    def __output_students(selfself,list_target):
        for stu in list_target:
            print("%d--%s--%d--%d"%(stu.id,stu.name,stu.age,stu.score))

    def __output_student_by_score(self):
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __delete_student(self):
        id = int(input("请输入需要删除的学生编号："))
        if self__manager.remove_student(id):
            print("删除失败")
        else:
            print("删除失败")


view = StudentManagerView()
view.main()
controller = StudentManagerController()
controller.add_student(StudentModel("zs", 12, 21))
for item in controller.list_stu:
    print(item.id, item.name, item.age, item.score)

stu = StudentModel()
stu.name = input("请输入姓名：")
stu.age = int(input("请输入年龄："))
stu.score = int(input("请输入成绩："))
self.__manager.add_student(stu)
print(self.__manager)