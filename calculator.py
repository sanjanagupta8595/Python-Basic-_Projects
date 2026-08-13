# CALCULATOR

val_1 = input("ENTER YOUR 1ST NUMBER : ")
val_2 = input("ENTER YOUR 2ND NUMBER : ")
operation = input("ENTER YOUR OPERATION : ")

expression = val_1 + operation + val_2
result = eval(expression)
print(result)
