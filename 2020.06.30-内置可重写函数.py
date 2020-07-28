class Wife:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        #返回给人看
        return "奴家叫：%s,年芳：%d"%(self.name,self.age)
    def __repr__(self):
        #返回给解释器看
        return 'Wife("%s",%d)'%(self.name,self.age)

w01 = Wife("金莲",23)
print(w01)#将对象转换成字符串
re = eval("1+4")#python 代码
print(re)
w02 = eval('Wife("金莲",23)')
print(w02)
#w03 =eval(input("qw"))
w04 = eval(w01.__repr__())#克隆w01对象__将给机器解释的对象字符串转变成为元组
w01.name ="莲莲"
print(w04.name)
print(w01.__dict__)
print(w04.__dict__)