import mysql.connector

def connect_to_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        database='unifier',
        password='rootpass',
        port=3306
    )

    return conn