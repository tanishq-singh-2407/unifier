from db.passwords import get
from lib.promt import choose
import pandas as pd
import pyperclip

show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def add_passwords(first_name: str, last_name: str, email: str, password: str):
    print(show.format(first_name, last_name, email))

    return input("\nPress any button to exit")