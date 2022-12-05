from db import connect
from mysql.connector import DatabaseError
from cryptocode import decrypt

def get_all_passwords(email, password):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("SELECT * FROM passwords WHERE user_email='%s'" % (email,))
        data = [[unit[0], unit[1], unit[2], unit[3], decrypt(unit[4], password)] for unit in cur.fetchall()]

        return data

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()