def calculate_grade(m1, m2, m3):
    avg_mark = (m1+m2+m3)/3

    if avg_mark >= 90:
        grade = "A"
    elif avg_mark >=80:
        grade = "B"
    elif avg_mark >=70:
        grade = "C"
    elif avg_mark >=60:
        grade = "D"
    else:
        grade = "F"

    return avg_mark, grade 

marks1 = float(input("Enter Makrs of 1st Subject: "))
marks2 = float(input("Enter Makrs of 2nd Subject: "))
marks3 = float(input("Enter Makrs of 3rd Subject: "))


result = calculate_grade(marks1, marks2, marks3)

print(result)
