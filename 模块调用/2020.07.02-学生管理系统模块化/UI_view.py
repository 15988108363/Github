__doc__ = "表示层"
import model,UI_view,bll_controller
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
            pass
        if number == 5:
            bll_controller.StudentManagerController.order_by_score()

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