 
username = "admin"
password = "admin123"

user = input("Enter Username: ")
passw = input("Enter password: ")

if user == username and passw == password:
    print("login Successful!")
elif  passw != password:
    print("Incorrect password!")
elif user != username:
    print("Incorrect Username!")
    