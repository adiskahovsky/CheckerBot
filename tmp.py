import  pymysqlData
import pymysql


connect = pymysql.connect(host=pymysqlData.host,  # your host, usually localhost
                          user=pymysqlData.user,  # your username
                          passwd=pymysqlData.passwd,  # your password
                          db=pymysqlData.db,
                          charset=pymysqlData.charset)

cursor = connect.cursor()


cursor.execute("SELECT * FROM keywords WHERE id=36546")
print(cursor.fetchall())

connect.close()