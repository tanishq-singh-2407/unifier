from db.users.auth import login_user

h = login_user(
    email="hlo@hlo.com",
    password="hlohlo"
)

print(h)