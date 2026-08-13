print("            Restaurant Bill Calculator           ")

a = input("1st item : ")
a1 = float(input("price : "))

b = input("2nd item : ")
b1 = float(input("price : "))

c = input("3rd item : ")
c1 = float(input("price : "))

subtotal = a1+b1+c1
print("TAX INCLUDING")
tax = subtotal*0.05
final_total = subtotal + tax

print("TOTAL AMOUNT TO PAY : ",final_total)
print("THANKU FOR ORDER")
print("HAVE A NICE DAY!!!")
