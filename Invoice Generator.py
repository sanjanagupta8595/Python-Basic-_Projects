print("          Invoice Generator           ")

a = input("1st item name : ")
cost1 = int(input("Price : "))
quant1 = int(input("How many Quantity : "))

b = input("2nd item name : ")
cost2 = int(input("Price : "))
quant2 = int(input("How many Quantity : "))

c = input("3rd item name : ")
cost3 = int(input("Price : "))
quant3 = int(input("How many Quantity : "))

total = cost1*quant1 +cost2*quant2 + cost3*quant3
print(" TOTAL BILL : ", total)

print("CONGRATULATIONS!!!")
print("YOUR INVOICE IS GENERATED")
