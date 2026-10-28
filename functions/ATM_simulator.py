def withdraw(balance, amount):
    if amount <=0:
        return "Invaid Amount"
    elif amount > balance:
        return "Insufficient Funds"
    else:
        return balance - amount
    
balance = int(input("Enter Account Balance: "))
amount = int(input("Enter the Withdrawal amount: "))

print(withdraw(balance, amount))