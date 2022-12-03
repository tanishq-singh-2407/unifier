from lib import promt, login, register

type_ask = """
              UNIFIER

------------ SELECT ONE ------------
1. Register (new user)
2. Login (old user)

type (default 2): 
"""

def main():
    type = promt.ask_message(message=type_ask, default=2)

    if int(type) == 1:
        register.register_user()

    else:
        login.login_user() 


if __name__ == "__main__":
    main()