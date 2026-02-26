from tools import calculate_vat, greet_customer

# create total bill variable
total_bill = 1000

# 2. call greet_customer function
customer_name = "Tony"
greeting = greet_customer(customer_name)
print(greeting)

# 3. call calculate_vat function
vat_amount = calculate_vat(total_bill)
print(f"Total bill: {total_bill}")
print(f"VAT amount: {vat_amount}")
print(f"Total bill including VAT: {total_bill + vat_amount}")