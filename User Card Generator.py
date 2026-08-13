# # USER CARD GENERATOR

print("USE CAPITAL LETTERS")

name1 = input("Enter your First Name : ")
name2 = input("Enter your Last Name: ")

print("Enter your full date of birth information")
date = int(input("Enter yout date of brith : "))
month = input("Enter your Month of birth : ")
year = int(input("Enter your year of birth : "))

phone = int(input("Enter your Phone no. : "))
email = input("Enter your Email Address : ")

print("Enter your Full Address ") 
house = int(input("Enter your House No. : "))
street = int(input("Enter your Street No. : "))
street_1 = input("Enter your Street name : ")
city = input("Enter your City : ")
state = input("Enter your State : ")
pincode = int(input("Enter your Pincode : "))

print("Enter About yourself")
job = input("Enter your Profession : ")
hobby = input("Enter your Hobby : ")


print("YOUR USER CARD")
print("FULL NAME : ", name1 ,name2)
print("D.O.B : ", date , month , year)
print("PHONE NO. : ", phone)
print("EMAIL ID : ")
print("LOCATION : ", house ,"GALI NO.-",street ,street_1 ,city ,state ,pincode)
print("PROFESSION : ", job)
print("HOBBY : ", hobby)

print("CONGRATULATIONS!!!")
print("YOU SUCCESSFULLY GENERATED YOUR USER ID CARD")