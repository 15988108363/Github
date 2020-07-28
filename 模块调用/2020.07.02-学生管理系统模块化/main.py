__doc__ = "程序入口"
#==================主程序测试============================
from model import *
from  UI_view import *
from bll_controller import *

if __name__ == "__main__":
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