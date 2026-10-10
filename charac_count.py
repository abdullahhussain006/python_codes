
text = input("Enter a String: ")


characters = 0
spaces = 0
digits = 0
alphabets = 0


for i in text:
    if i.isalnum():
        characters+=1
    if i == " ":
        spaces+=1
    if i.isdigit():
        digits+=1
    if i.isalpha():
        alphabets+=1


print("\nNumber of Characters: ", len(text))
print("Letter and Digits: ", characters )
print("Number of alphabets: ", alphabets )
print("Number of spaces: ", spaces )
print("Number of digits: ", digits )