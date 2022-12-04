from os import system, name
from emoji import emojize 
from getpass import getpass

def clear_screen():
    if name == 'posix':
        system('clear')

    else:
        system('cls')

def password(message: str, show: str = "", minLength: int = 1, maxLength: int = None, clear_at_start: bool = True) -> str:
    ans = ""

    if clear_at_start:
        clear_screen()

    while True:
        if show != "":
            print(show)

        ans = getpass(
            str(message) + ": "
        )
        clear_screen()

        if maxLength and len(ans) > maxLength:
            print("Password is to long (max {0})".format(maxLength))

        elif len(ans) < minLength:
            print("Password is to short (min {0})".format(minLength))

        else:
            return str(ans)
        

def message(message: str, show: str = "", minLength: int = 1, maxLength: int = None, default=None, clear_at_start: bool = True) -> str:
    ans = ""
    default_txt = ("\n   [default: " + str(default) + "]") if default != None else ""

    if clear_at_start:
        clear_screen()

    while True:
        if show != "":
            print(show)

        ans = input(
            emojize(
                ":sauropod: " + str(message) + default_txt + ": "
            )
        )
        clear_screen()

        if maxLength and len(ans) > maxLength:
            print("String is to long (max {0})".format(maxLength))

        elif len(ans) < minLength:
            if default:
                return str(default)

            else:
                print("String is to short (min {0})".format(minLength))

        else:
            return str(ans)

def choose(message: str, enum: list[str], show: str = "", default=None, clear_at_start: bool = True):
    ans = ""
    options = "".join([("   " + str(i + 1) + ") " + str(enum[i]) + "\n") for i in range(len(enum))])
    default_txt = (", [default: " + str(default) + "]") if default != None else ""

    if clear_at_start:
        clear_screen()

    while True:
        if show != "":
            print(show)
            
        ans = input(
            emojize(
                ":sauropod: " + str(message) + "?\n"
                + options
                + "\n:beetle:  Enter here" + default_txt + ": "
            )
        )
        clear_screen()

        try:
            if int(ans) <= len(enum):
                return int(ans)

        except ValueError:
            if default != None:
                return int(default)


def confirm(message: str, show: str = "", default: bool=None, clear_at_start: bool = True) -> str:
    ans = default
    options = ", " + ("[y/n]" if default == None else "[Y/n]" if default else "[y/N]")

    if clear_at_start:
        clear_screen()

    while True:
        if show != "":
            print(show)

        ans = input(
            emojize(
                ":sauropod: " + message + options + ": "
            )
        )
        clear_screen()

        if ans.lower() == "y" or ans.lower() == "n":
            return ans.lower() == "y"

        elif default != None:
            return ("y" if default else "n") == "y"