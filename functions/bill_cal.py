def calculate_bill(price, quantity, discount):
    bill = price*quantity
    discount_cal = (discount/100)*bill

    return bill - discount_cal
    


price = int(input("Enter Product Price: "))
quantity = int(input("Enter Product Quantity: "))
discount = int(input("Enter Discount Percentage: "))

calculated_bill = calculate_bill(price, quantity, discount)

print(calculated_bill)