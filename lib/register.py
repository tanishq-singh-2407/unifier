from lib.promt import ask_message
from db.users.get import get_user
from db.users.auth import register_user

def register_user():
    print("\n\n\n\nREGISTER NEW USER\n")
    first_name = ask_message("Enter first name: ", 3, 30)
    last_name = ask_message("Enter last name: ", 3, 30)
    email = ask_message("Enter email id: ", 3, 60)

    if get_user(email) is not None:
        print("User with email: {0}, already exits".format(email))

    else:
        id = register_user(first_name, last_name, email)

        if id is None:
            print("There was some error registering you.")

        else:
            print("You are registered.")