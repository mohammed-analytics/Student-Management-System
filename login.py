import json

def login():

    file = open("user.json", "r")
    users = json.load(file)
    file.close()

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:

        if user["username"] == username and user["password"] == password:

            print("Login successful!")
            return True

    print("Invalid username or password")
    return False
login()