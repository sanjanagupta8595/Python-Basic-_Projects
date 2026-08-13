import random
print("        RANDOM PASSWORD GENERATOR (with name)        ")

name = input("Enter your First Name without space: ") 
print("Length of the Name : ",len(name))                                                                                     
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#^%$&*()_-+=|.,"
k = int(input("How many extra letters/numbers you want to add with your name : "))
random1 = "".join(random.choices(chars,k=k))

pswd = name+random1
print(pswd)