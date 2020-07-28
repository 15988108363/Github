class Graphics_Manager:
    graphics_list =[]
    def __init__(self):
        self.graphics_temp_dict = {}
    def put_in_graphics_list(self,shape,value):#将图形、面积放入图形容器
        self.area = value
        self.shape =shape
        self.graphics_temp_dict[self.shape] = self.area
        Graphics_Manager.graphics_list.append(self.graphics_temp_dict)
        print(Graphics_Manager.graphics_list)
    def print_self(self):#打印具有的所有图形
        print(Graphics_Manager.graphics_list)
        for gra in Graphics_Manager.graphics_list:
            for key,value in gra.items():
                print(key,":",value)
        print("完毕")
    def Calculating_Total_area(self): #计算所有图形的总面积
        total_area = 0
        for gra in Graphics_Manager.graphics_list:
            for key in gra:
                total_area += gra[key]
        print("所有图形总面积为：%0.4f"%total_area)
    def computing_method(self,odj):#多态
        obj.computing_method

class Roundness(Graphics_Manager):#圆形计算
    def __init__(self,radius):
       self.radius = radius
       super().__init__()
    def computing_method(self):
        area = self.radius* 3.1415926 *2
        print("该圆形的面积：%0.4f" %area)
        super().put_in_graphics_list("圆形面积：",area)

class Rectangle(Graphics_Manager):
    def __init__(self,longth,width):
       self.longth = longth
       self.width = width
       super().__init__()
    def computing_method(self):
        area = self.longth * self.width
        print("该矩形的面积：%0.4f"%area)
        super().put_in_graphics_list("矩形面积：",area)

class Trapezoid(Graphics_Manager):
    def __init__(self,up_bottom,down_bottom,high):
       self.up_bottom = up_bottom
       self.down_bottom = down_bottom
       self.high = high
       super().__init__()
    def computing_method(self):
        area = (self.up_bottom + self.down_bottom)*self.high/2
        print("该梯形的面积：%0.4f"%area)
        super().put_in_graphics_list("梯形面积：",area)

r01 =Rectangle(6,7)
r01.computing_method()
r02 =Roundness(34)
r02.computing_method()
t01 =Trapezoid(23,32,4)
t01.computing_method()
g01 = Graphics_Manager()
g01.print_self()
g01.Calculating_Total_area()