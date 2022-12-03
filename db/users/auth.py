from db import connect
from mysql.connector import DatabaseError

def register_user(first_name: str, last_name: str, email: str) -> str | None:
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("INSERT INTO users (first_name, last_name, email) VALUES ('%s', '%s', '%s')" % (first_name, last_name, email))
        conn.commit()
        
        return email

    except DatabaseError as e:
        print(e.msg)
        return None

    finally:
        cur.close()
        conn.close()

def delete_user(email: str) -> bool:
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("DELETE FROM users WHERE email='%s'" % (email,))
        conn.commit()
        
        return True

    except DatabaseError as e:
        print(e.msg)
        return False

    finally:
        cur.close()
        conn.close()