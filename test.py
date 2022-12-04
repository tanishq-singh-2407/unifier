from lib.user import login
from db.passwords import delete

login.logged_in(
    first_name="Tanvii",
    last_name="Singh",
    email="tanviisingh640@gmail.com",
    password="tanvii-2301"
)

# dt = delete.delete_one(
#     email='tanviisingh640@gmail.com',
#     id=100
# )

# print(dt)