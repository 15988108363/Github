#import module01#调用模块，并赋值给名为module01的变量
#module01.fun01()
#c01 = module01.MyClass01()
#c01.fun02()
#=======================程序结果==============================
#我是module01
#fun01
#fun02
#-----------------------第二种导入方式-------------------------
#from module01 import fun01,MyClass01
#fun01()
#c01 = MyClass01()
#c01.fun02()
#=======================程序结果==============================
#我是module01
#fun01
#fun02
#-----------------------第三种导入方式-------------------------
#from module01 import *#对多模块非常熟悉，可以用*
#fun01()
#c01 = MyClass01()
#c01.fun02()
#c04 = fun04()
#c03 = fun03()#未添加入__all__
#=======================程序结果==============================
#我是module01
#fun01
#fun02
#fun04
#NameError: name 'fun03' is not defined
#-----------------------第三种导入方式-------------------------
#from module01 import *
#fun01()
#print(__doc__)
#=======================程序结果==============================
#我是module01
#fun01
#None
#-----------------------第一种导入方式-------------------------
#import module01
#print(__doc__)文档注释
#=======================程序结果==============================
#我是module01
#None
#-----------------------第一种导入方式-------------------------
import module01
print(module01.__doc__)
print(__file__)
print(__name__)
#=======================程序结果==============================
#我是module01
#['这是module01模块']
#D:/PyCharm——练习文件/模块调用/2020.07.02-模块调用范例-module01.py
#__main__
