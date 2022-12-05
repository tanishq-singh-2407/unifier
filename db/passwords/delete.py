from db import connect
from mysql.connector import DatabaseError

def delete_one(email, id):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("DELETE FROM passwords WHERE user_email='%s' AND id='%s'" % (email, id))
        conn.commit()

        return True

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()

def delete_all(email):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("DELETE FROM passwords WHERE user_email='%s'" % (email,))
        conn.commit()

        return True

    except DatabaseError as e:
        print(e.msg)

    finally:
        cur.close()
        conn.close()