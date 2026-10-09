

price = int(input("Enter Product Price: "))

quantity = int(input("Enter Product Quantity: "))

discount = int(input("Enter Discount Price: "))


total_price = price * quantity
total_dis = discount/100 * total_price
final_bill  = total_price - total_dis

print("-----------Total Bill-------------")
print("\nTotal Price: ", total_price)
print("Quantity: ", quantity)
print("Discount: ", discount)
print("Final Bill: ", int(final_bill))
print("----------------------------------")