from db.passwords import get
import csv

def export_all(email, password):
    file_name = "passwords.csv"
    passwords = get.get_all_passwords(email, password)

    file = open(file_name, mode="w", newline='', encoding='utf-8')
    file_writer = csv.writer(file)

    file_writer.writerow(["id", "user_email", "site_url", "username", "password"])
    file_writer.writerows(passwords)

    print("File exported (name: {0})".format(file_name))
    return input("\nPress any to return")