import time
#返回时间戳（1970年后经过的浮点数）
#1555579061.7284493
print(time.time())
#时间戳 ————》时间元组（年月日时分秒星期，一年的第几天）
print(time.localtime(155579061.7284493))
#时间元组 ——》时间戳
print(time.mktime(time.localtime()))
#时间的格式化
#时间元组--》字符串
print(time.strftime("%Y %m %d %H:%M:%S",time.localtime()))
#字符串 --》时间元组
print(time.strptime("2020 07 02 16:49:43","%Y %m %d %H:%M:%S"))

"""def Calculate_the_day_of_the_week(year,month,day):
    str01 = str(year)+" "+str(month)+" "+ str(day)
    tuple01 = time.strptime(str01, "%Y %m %d")
    print("这天是星期%s"%(tuple01[6]+1))"""
def Calculate_the_day_of_the_week(*args):
    item =str(args[0])
    for i in range(len(args)-1):
        item = item +" "+ str(args[i+1])
    tuple01 = time.strptime(str(item), "%Y %m %d")
    print("这天是星期%s" % (tuple01[6] + 1))

def lived_day(year,month,day):
    str01 = str(year) + " " + str(month) + " " + str(day)
    day01 = time.mktime(time.strptime(str01,"%Y %m %d"))
    day_lived = (time.time()-day01)//86400
    print("总共活了%s天"%day_lived)

def get_week(year,month,day):
    time_tuple = time.strptime("%s %s %s"%(year,month,day),"%Y %m %d")
    weeks= {0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日",}
    print(weeks[time_tuple[6]])

def life_day(year,month,day):
    time_tuple = time.strptime("%s %s %s"%(year,month,day),"%Y %m %d")
    day_lived = (time.time()-time.mktime(time_tuple))//86400
    print("总共活了%s天"%day_lived)

Calculate_the_day_of_the_week(2020,7,2)
lived_day(2020,1,1)
get_week(2020,7,2)
life_day(2020,1,1)