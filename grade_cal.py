
marks = int(input("Enter Marks: "))


while marks < 0 or marks > 100:
    print("Number is Negative! Enter Positive Number")
    marks = int(input("Enter Marks: "))

     

if marks >= 90 and marks <= 100:
    print("Your grade A")
elif marks >= 80 and marks <= 89:
    print("Your grade is B")
elif marks >= 70 and marks <= 79:
    print("Your grade is C")
elif marks >= 60 and marks <= 69:
    print("Your grade is D")
elif marks >= 50 and marks <= 59:
    print("Your grade is E")
elif marks <= 50:
    print("Your grade is F")