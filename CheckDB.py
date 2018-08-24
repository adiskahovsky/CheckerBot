import pymysql
import pymysqlData
import time

class CheckDB:
    def __init__(self):
        #while True:
            connect = pymysql.connect(host=pymysqlData.host,  # your host, usually localhost
                                      user=pymysqlData.user,  # your username
                                      passwd=pymysqlData.passwd,  # your password
                                      db=pymysqlData.db,
                                      charset=pymysqlData.charset)
            cursor = connect.cursor()
            try:
                #while True:

                    #for i in range(5):
                    cursor.execute("SELECT * FROM news WHERE is_posted='Yes'")
                    result = cursor.fetchall()
                    #print(result)
                    if result !=():
                        #print('work1')
                        for i in result:
                            id = i[2]
                            link = i[7]
                            cursor.execute("SELECT * FROM keywords WHERE id={}".format(id))
                            data = cursor.fetchone()
                            title_id = data[6]
                            #print(data[6])
                            #print(link)
                            cursor.execute("SELECT chat_id FROM chat_id WHERE title_id='{}'".format(title_id))
                            print(cursor.fetchone())
                        #time.sleep(40)

                        #cursor.execute("SELECT * FROM keywords")
                        #print(cursor.fetchall())
                        time.sleep(40)


            except Exception:
                time.sleep(1)
                connect.close()



def main():

    """
    connect = pymysql.connect(host="92.53.120.227",  # your host, usually localhost
                         user="user",  # your username
                         passwd="soCI19al",  # your password
                         db="social",
                         charset='utf8mb4')
    """

    obj = CheckDB()
if __name__=='__main__':
    main()
