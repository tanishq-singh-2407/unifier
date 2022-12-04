from db import connect
from mysql.connector import DatabaseError

def get_all_passwords(email: str, password: str):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("SELECT * FROM passwords WHERE user_email='%s'" % (email,))
        data = cur.fetchall()

        return data

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()