from lib.promt import message, confirm, password
from db.users.get import get_user
from db.users.auth import delete_user as auth_delete_user

def delete_user():
    email = message(message="Enter email id", minLength=3, maxLength=60, clear_at_start=False)

    is_correct_information = confirm(
        message="Is above information correct",
        show=(
            "Your Details\n\n"
            + "Email Id   : " + email + "\n"
        ),
        default=True
    )

    if is_correct_information:
        if "@" in email and "." in email:
            already_registered_user = get_user(email)

            if already_registered_user:
                user_password = password(message="Enter password", minLength=5, maxLength=30)
                
                if auth_delete_user(email, user_password):
                    print("User Deleted with email: {0}".format(email))
                    quit()

                else:
                    print("Password didn't matched")

            else:
                print("User with (email: {0}) dosen't exist".format(email))

        else:
            print("Enter a correct Email-Id")
        
    delete_user() if confirm(message="Do you want to re-try", default=True, clear_at_start=False) else quit()