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

    match type:
        case 1:
            register_user()

        case 2:
            login_user()

        case 3:
            delete_user()

        case _:
            quit()

if __name__ == "__main__":
    main()