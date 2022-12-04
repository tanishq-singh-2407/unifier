from lib.promt import choose, message, confirm, password, clear_screen
from db.users.get import get_user
from db.users.auth import login_user as auth_login_user
from lib.password import add, get, export_csv, import_csv, delete


show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def logged_in(first_name: str, last_name: str, email: str, password: str):
    clear_screen()

    while True:
        type = choose(
            message="Choose any one",
            show=show.format(first_name, last_name, email),
            default=6,
            enum=[
                "Get Password",
                "Add Password",
                "Delete Password",
                "Import Passwords from CSV",
                "Export Passwords from CSV",
                "Logout"
            ]
        )

        match type:
            case 1:
                get.list_all_passwords(first_name, last_name, email, password)

            case 2:
                add.add_passwords(first_name, last_name, email, password)

            case 3:
                delete.delete_password(first_name, last_name, email, password)

            case 4:
                import_csv.import_all(first_name, last_name, email, password)

            case 5:
                export_csv.export_all(email, password)

            case _:
                quit()

def login_user():
    email = message(message="Enter email id", minLength=3, maxLength=60, clear_at_start=False)

    is_correct_information = confirm(
        message="Is above information correct",
        show=("Email Id   : " + email + "\n"),
        default=True
    )

    if is_correct_information:
        if "@" in email and "." in email:
            already_registered_user = get_user(email)

            if already_registered_user:
                user_password = password(message="Enter password", minLength=5, maxLength=30)
                
                if auth_login_user(email, user_password):
                    return logged_in(
                        first_name=already_registered_user[0],
                        last_name=already_registered_user[1],
                        email=email,
                        password=user_password
                    )

                else:
                    print("Password didn't matched")

            else:
                print("User with (email: {0}) dosen't exist".format(email))

        else:
            print("Enter a correct Email-Id")
        
    login_user() if confirm(message="Do you want to re-try", default=True, clear_at_start=False) else quit()