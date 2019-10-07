import ReadTask
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='python_db',
)
exec('ReadTask')

ids = input("Enter id of your task to be updated: ")
title = input("Enter title of your task: ")
desc = input("Add some description to it: ")

try:
    with con.cursor() as cursor:
        sql = "UPDATE todos SET `title`=%s, `desc`=%s WHERE `id` = %s"
        try:
            cursor.execute(sql, (title, desc, ids))
            print("Successfully Updated...")
            sql = "SELECT `id`, `title`, `desc` FROM todos"
            try:
             cursor.execute(sql)
             result = cursor.fetchall()
 
             print("Id\t\tTitle\t\t\t\t\tDescription")
             print("-"*80)
             #print(result)
             for row in result:
                print(str(row[0]) + "\t\t" + row[1] + "\t\t\t\t\t" + row[2])
 
            except:
             print("Oops! Something wrong")
        except:
            print("Oops! Something wrong")
 
    con.commit()
finally:
    con.close()
