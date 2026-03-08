users = {}
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    users[username] = password
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


def check_password():
    username = input("Enter username: ")

    if username in users:
        print("Password:", users[username])
    else:
        print("User not found")


while True:

    print("1.Register")
    print("2.Login")
    print("3.View Users")
    print("4.Check Password")
    print("5.Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        view_users()

    elif choice == "4":
        check_password()

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid option")