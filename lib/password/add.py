from lib.promt import message, confirm
from db.passwords import add

show = """                 UNIFIER
-----------  Password Manager  -----------


Welcome  : {0} {1}
Email Id : {2}
"""

def get_data(first_name, last_name, email):
    site_url = message(message="Enter site url", show=show.format(first_name, last_name, email), minLength=3 ,maxLength=255)
    username = message(message="Enter username", show=show.format(first_name, last_name, email), minLength=3 ,maxLength=255)
    password = message(message="Enter password", show=show.format(first_name, last_name, email), minLength=3 ,maxLength=255)

    is_correct_information = confirm(
        message="Is above information correct",
        show=(
            "Details\n\n"
            + "Site URL : " + site_url + "\n"
            + "Username : " + username + "\n"
            + "Password : " + password + "\n"
        ),
        default=True
    )

    return [site_url, username, password] if is_correct_information else False

def add_passwords(first_name, last_name, email, password):
    data = []

    while True:
        data = get_data(first_name, last_name, email)

        if data == False:
            if confirm(message="Do you want to re-try", show=show.format(first_name, last_name, email), default=True) == False:
                break

        else:
            add.add_one(
                user_email=email,
                user_password=password,
                site_url=data[0],
                username=data[1],
                password=data[2]
            )
            break

    return input("\nPress any button to exit")