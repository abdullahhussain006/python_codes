def calculate_salary(basic_sal, bonus = 0, tax_rate = 10):

    final_sal = (basic_sal + bonus)*(1 - (tax_rate/100))

    return final_sal


basic_sal = int(input("Enter Basic Salary: "))
bonus = input("Enter Bonus: ")
tax_rate = input("Enter Tax Rate %: ")


if bonus == "":
    bonus = 0
else:
    bonus = int(bonus)
if tax_rate == "":
    tax_rate = 10
else:
    tax_rate = float(tax_rate)   

final_sal  = calculate_salary(basic_sal, bonus, tax_rate)
print(f"Final Salary: {final_sal:.2f}")