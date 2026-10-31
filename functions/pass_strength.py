def check_pass(password):
    length = len(password) >= 8
    digit = any(digit.isdigit() for digit in password)
    upper = any(upper.isupper() for upper in password)

    return length and digit and upper 


password = input("Enter a Password: ")

check = check_pass(password)

print(check)