import json
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except:
    users = {}


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)


def register():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == "":
        print("Error: Username cannot be empty.")
        return

    if username in users:
        print("Error: Username already exists.")
    else:
        users[username] = password
        save_users()
        print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed!")


def view_users():
    print("Registered users:")
    for user in users:
        print(user)


while True:

    print("\n1. Register")
    print("2. Login")
    print("3. View Users")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        view_users()

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid option")