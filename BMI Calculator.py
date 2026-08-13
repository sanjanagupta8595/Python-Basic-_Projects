print("               BMI CALCULATOR              ")

weight = float(input("ENTER YOUR WEIGHT IN kg : "))
height = float(input("ENTER YOUR HEIGHT IN feet : "))

formula= weight/(height*3.28084)**2

print("YOUR BMI IS : ",round(formula,2))