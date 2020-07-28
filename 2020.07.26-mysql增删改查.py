"""pymysql增删改查"""
import pymysql
#连接数据库
db = pymysql.connect(host="localhost",port=3306,user= "root",
                     password="Q13470819781q",database="exercise",
                     charset= "utf8mb4")
#获取游标
cur = db.cursor()

name =input("name:")
age= input("age:")
sex = input("sex:")
score= input("score:")

# sql ="""insert into class_1 (name,age,sex,score) \
# values (%s,%d,%s,%f);"""%(name,age,sex,score)
# try:
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()#回滚到操作之前的状态
sql ="insert into class_1 (name,age,sex,score) \
values (%s,%s,%s,%s);"#不需要强转格式

try:
    cur.execute(sql,[name,age,sex,score])#自动识别参数类别
    db.commit()
except Exception as e:
    print(e)
    db.rollback()#回滚到操作之前的状态
#写操作
try:
    sql ="""insert into interest values \
    (8,"Bob","draw,sing","A","7777","凑合");"""#写入操作
    cur.execute(sql)
    sql = """update interest set price=6666 \
       where name="Abby";"""#更新操作
    cur.execute(sql)
    sql = """delete from class_1 where score<88;"""  # 删除操作
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print("出现异常为",e)
#读操作
sql = "select * from class_1 where age=13;"
#执行语句
cur.execute(sql)
one_row = cur.fetchone()
print(one_row)
maney_row = cur.fetchone(2)
print(maney_row)
all_row = cur.fetchall()
print(all_row)
cur.close()
db.close()