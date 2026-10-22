print("WELCOME TO GOURI JAISWAL'S SHOPPING MALL")
name=input("Enter your name:")#info of customer
phone=int(input("Enter your phone number:"))# info of customer

item1=input("Enter item1 name:")#info of item
price1=int(input("Enter item1 price:"))#info of item

item2=input("Enter item2 name:")#info of item
price2=int(input("Enter item2 price:"))#info of item

item3=input("Enter item3 name:")#info of item
price3=int(input("Enter item3 price:"))#info of item

TOTAL_BILL=price1+price2+price3#total bill amount
print("\nTHE TOTAL BILL AMOUNT")
print("Customer Name:",name)
print("Customer Phone Number:",phone)
print(item1,":Rs.",price1)
print(item2,":Rs.",price2)
print(item3,":Rs.",price3)
print("Total Amount To Be Paid:",TOTAL_BILL)
print("Thank You For Shopping With Us!",name)