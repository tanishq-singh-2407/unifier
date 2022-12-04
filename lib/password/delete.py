from db.passwords import delete, get
from lib.promt import choose
import pandas as pd
import pyperclip

show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def delete_password(first_name: str, last_name: str, email: str, password: str):
    passwords = get.get_all_passwords(email, password)

    type = choose(
        message="Choose any one",
        show=show.format(first_name, last_name, email),
        default=len(passwords) + 2,
        enum=[unit[2] for unit in passwords] + ["Delete All Passwords", "Go Back"]
    )

    if type == len(passwords) + 2:
        return

    else:
        print(show.format(first_name, last_name, email))

        if type == len(passwords) + 1: # Delete all passwords
            delete.delete_all(email)
            print("All passwords deleted.")

        else: # Delete selected one only
            unit = passwords[type - 1]
            delete.delete_one(email, unit[0])

            print("Deleted password for site: {0}".format(unit[2]))

        return input("Press any button to exit")