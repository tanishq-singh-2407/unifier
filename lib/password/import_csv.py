from lib.promt import choose, confirm
from db.passwords import add
from os import listdir
import csv
import pandas as pd

show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def import_all(first_name, last_name, email, password):
    files = [i for i in listdir() if i.endswith(".csv")]

    type = choose(
        message="Choose any one",
        show=show.format(first_name, last_name, email),
        default=len(files) + 1,
        enum=files + ["Go Back"]
    )

    if type == len(files) + 1:
        return

    else:
        print(show.format(first_name, last_name, email))

        file = open(files[type - 1], mode="r")
        file_reader = csv.reader(file)

        table = [row for row in file_reader]
        first_row = table[0]

        if "site_url" in first_row and "username" in first_row and "password" in first_row:
            site_url_index = first_row.index("site_url")
            username_index = first_row.index("username")
            password_index = first_row.index("password")

            dt = [[row[site_url_index], row[username_index], row[password_index]] for row in table[1:]]
            df = pd.DataFrame(dt, columns=['Site URL', 'Username', 'Password'], index=[i + 1 for i in range(len(dt))])

            print(df, end="\n\n\n")

            confirmation = confirm(
                message="Confirm Add",
                default=True,
                clear_at_start=False
            )

            if confirmation:
                for i in dt:
                    add.add_one(
                        user_email=email,
                        user_password=password,
                        site_url=i[0],
                        username=i[1],
                        password=i[2],
                    )

        else:
            print("CSV file must have row ('site_url', 'username', 'password')")

    return input("\nPress any key to go back.")