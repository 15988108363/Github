"""pymysql流程"""
import pymysql
#连接数据库
db = pymysql.connect(host="localhost",port=3306,user= "root",
                     password="Q13470819781q",database="exercise",
                     charset= "utf8mb4")
#获取游标
cur = db.cursor()
#数据操作
#执行sql语句
cur.execute("insert into class_1 values (11,'Eas',11,'w',86.5);")
#将修改内容提交到数据库
db.commit()
#关闭游标和数据库链接
cur.close()
db.close()