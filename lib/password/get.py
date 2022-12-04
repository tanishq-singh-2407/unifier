from db.passwords import get
from lib.promt import choose
import pandas as pd
import pyperclip

show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def list_all_passwords(first_name: str, last_name: str, email: str, password: str):
    passwords = get.get_all_passwords(email, password)

    type = choose(
        message="Choose any one",
        show=show.format(first_name, last_name, email),
        default=len(passwords) + 2,
        enum=[unit[2] for unit in passwords] + ["List All Passwords", "Go Back"]
    )

    if type == len(passwords) + 2:
        return

    else:
        print(show.format(first_name, last_name, email))

        if type == len(passwords) + 1:
            dt = [[unit[2], unit[3], unit[4]] for unit in passwords]
            df = pd.DataFrame(dt, columns=['Site URL', 'Username', 'Password'], index=[i + 1 for i in range(len(passwords))])

            print(df, end="\n\n\n")

        else:
            unit = list(list(passwords)[type - 1])

            d = [[unit[2], unit[3], unit[4]]]
            df = pd.DataFrame(d, columns = ['Site URL', 'Username', 'Password'])
            
            pyperclip.copy(unit[4])

            print(df)
            print("\nPassword has been copied")

        return input("Press any button to exit")