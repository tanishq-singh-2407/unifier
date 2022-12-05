from db import connect
from mysql.connector import DatabaseError

def get_all_users():
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users")

        return cur.fetchall()

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()

def get_user(email):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email='%s'" % (email,))

        return cur.fetchone()

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()