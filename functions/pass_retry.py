
correct_password = "password123"

passw = input("Enter Password: ")

while passw != correct_password:
    passw = input("Enter Password Again: ")

if passw == correct_password:
    print("Access Granted!")