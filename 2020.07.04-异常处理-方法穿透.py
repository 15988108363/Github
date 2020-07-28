class Wife:
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 20 <= value <= 30:
            self.__age =value
        else:
            raise ValueError("我不要")#人为抛出异常

try:
    w01 = Wife(50)
except:
    print("知道了")