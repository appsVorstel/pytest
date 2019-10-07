import pymysql

def connect():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='python_db',
    )