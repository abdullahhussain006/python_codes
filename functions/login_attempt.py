correct_password = "user1234"

def login():
    for attempt in range(3):
        password = input("Enter password: ")

        if password == correct_password:
            return "Login Successful!"

        print("Incorrect password! Try again.")

    return "Account Temporarily Blocked"

print(login())