import pymysql
import time
#创建连接
now = time.time()
DB = pymysql.connect(host="localhost",
                     user= "root",
                     passwd= "root",
                     database= "exercise",
                     charset= "utf8mb4")
#创建游标
cur = DB.cursor()
#=========================放入图库===================================================
# with open (r"D:\PyCharm——练习文件\临时文件\Image\20160830_074429-1.jpg","rb") as fd:
#     date= fd.read()
# try:
#     sql = "insert into images values (1,'mysql01.jpg',%s)"
#     cur.execute(sql,[date])
#     DB.commit()
# except Exception as e:
#     print(e)
#     DB.rollback()
#========================获取文件====================================================
sql = "select * from images where filename='mysql01.jpg'"
cur.execute(sql)
image = cur.fetchone()
with open(r"D:\PyCharm——练习文件\临时文件\Image\image.jpg","wb") as fd:
    fd.write(image[2])
cur.close()
DB.close()
now =time.time()-now
print(now)