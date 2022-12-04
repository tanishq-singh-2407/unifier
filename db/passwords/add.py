from db import connect
from mysql.connector import DatabaseError

def add_one(user_email: str, site_url: str, username: str, password: str):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        cur.execute("INSERT INTO passwords (user_email, site_url, username, password) VALUES ('%s', '%s', '%s', '%s')" % (user_email, site_url, username, password))
        conn.commit()

        print("password for site: {0}, has been added".format(site_url))

        return True

    except DatabaseError as e:
        if e.sqlstate == "23000":
            print("password for site: {0}, already exists".format(site_url))

        else:
            print(e.msg)

    finally:
        cur.close()
        conn.close()