from db import connect
from mysql.connector import DatabaseError
from lib.cipher import Hashing
from db.users.get import get_user

def login_user(email: str, password: str) -> bool:
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        dt = get_user(email)

        if dt == None:
            return False

        else:
            return True if Hashing.check_hash(password, dt[4].encode()) else False

    except DatabaseError as e:
        print(e.msg)
        return False

    finally:
        cur.close()
        conn.close()

def register_user(first_name: str, last_name: str, email: str, password: str) -> str | None:
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        password_hash = Hashing.gen_hash(password).decode()

        cur.execute("INSERT INTO users (first_name, last_name, email, password_hash) VALUES ('%s', '%s', '%s', '%s')" % (first_name, last_name, email, password_hash))
        conn.commit()
        
        return email

    except DatabaseError as e:
        print(e.msg)
        return None

    finally:
        cur.close()
        conn.close()

def delete_user(email: str, password: str) -> bool:
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        if login_user(email, password):
            cur.execute("DELETE FROM users WHERE email='%s'" % (email,))
            conn.commit()
        
            return True

        else:
            return False

    except DatabaseError as e:
        print(e.msg)
        return False

    finally:
        cur.close()
        conn.close()