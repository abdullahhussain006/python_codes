
name = input("Enter Your Name: ")

age = int(input("Enter Your Age: "))

mark1 = float(input("Enter Subject 1 Marks: "))
mark2 = float(input("Enter Subject 2 Marks: "))
mark3 = float(input("Enter Subject 3 Marks: "))

total_marks = mark1 + mark2 + mark3

average_marks = total_marks / 3

print("-------------------------")
print("\nName: ", name)
print("Age: ",  age)
print("Total Marks", total_marks)
print(f"Average Marks: {average_marks:.2f}")

if total_marks >50:
       print("Result Status: Pass")
else:
      print("Result Status: Fail")

print("-------------------------")