

name = input("Enter your Name: ")\

if len(name) <= 5:
    print("Username contain less than 5 characters")
else:
    print("Usrname contain greater then 5 characters")

if any(i.isdigit() for i in name ): 
    print("Username contain Numbers")
else:
    print("Username does not contain Numbers") 

if any(i.isalpha() for i in name):
    print("Username contain Alphabets")
else:
    print("Usrname does not contain Alphabets")

if  " " in name:
    print("Username contain Spaces")
else:
    print("Username does not contain Spaces")