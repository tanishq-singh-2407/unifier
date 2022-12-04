from lib.promt import message, confirm, password
from db.users.get import get_user
from db.users.auth import register_user as auth_register_user

def register_user(first_name: str="", last_name: str="", email: str=""):
    if first_name == "":
        first_name = message(message="Enter first name", minLength=3, maxLength=30)
    
    if last_name == "":
        last_name = message(message="Enter last name", minLength=3, maxLength=30)

    if email == "":
        email = message(message="Enter email id", minLength=3, maxLength=60, clear_at_start=False)

    is_correct_information = confirm(
        message="Is above information correct",
        show=(
            "Your Details\n\n"
            + "First Name : " + first_name + "\n"
            + "Last Name  : " + last_name + "\n"
            + "Email Id   : " + email + "\n"
        ),
        default=True
    )

    if is_correct_information:
        if "@" in email and "." in email:
            already_registered_user = get_user(email)

            if already_registered_user != None:
                print("User with (email: {0}) already exists".format(email))
                register_user() if confirm(message="Do you want to re-try", default=True, clear_at_start=False) else quit()

            else:
                user_password = password(message="Enter password", minLength=5, maxLength=30)
                
                email_ = auth_register_user(first_name, last_name, email, user_password)

                if email_:
                    print("User Registered with email: {0}".format(email_))
                    quit()

        else:
            print("Enter a correct email Id")
            register_user(first_name, last_name)

    else:
        register_user() if confirm(message="Do you want to re-try", default=True) else quit()