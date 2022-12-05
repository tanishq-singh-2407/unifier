from lib.promt import choose
from lib.user.register import register_user
from lib.user.login import login_user
from lib.user.delete import delete_user

show = """                  UNIFIER
-----------  Password Manager  -----------

"""

def main():
    type = choose(
        message="Choose any one",
        show=show,
        default=4,
        enum=[
            "Register",
            "Login",
            "Delete Account",
            "Quit"
        ]
    )

    if type == 1: 
        register_user()

    elif type == 2:
        login_user()

    elif type == 3:
        delete_user()

    else:
        quit()

if __name__ == "__main__":
    main()