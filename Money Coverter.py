# MONEY CONVERTER

# now Exchange rate is 1 US Dollar = Rs 95.40
# so you can Enter your Current Exchange Rate = Rs 95.40

ind_rs = float(input("Enter your Indian Ruppes in Rs : Rs "))
current = float(input("Enter your Current Exchange Rate in Rs : Rs "))
Dollar = ind_rs/current
print("Converted Amount in USD : $",round(Dollar,2))