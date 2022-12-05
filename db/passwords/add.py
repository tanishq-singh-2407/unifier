from db import connect
from mysql.connector import DatabaseError
from cryptocode import encrypt

def add_one(user_email, user_password, site_url, username, password):
    try:
        conn = connect.connect_to_database()
        cur = conn.cursor()

        password_encode = encrypt(password, user_password)

        cur.execute("INSERT INTO passwords (user_email, site_url, username, password) VALUES ('%s', '%s', '%s', '%s')" % (user_email, site_url, username, password_encode))
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