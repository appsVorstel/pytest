import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='python_db',
)
try:
    with connection.cursor() as cursor:
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
 
    connection.commit()
finally:
    connection.close()