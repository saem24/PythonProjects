# Basic tax calculator with easy to modify criterias.

income = int(input("Please input your income in USD: "))

rate_for_mid_bracket = 0.1
rate_for_top_bracket = 0.2

no_tax_amt = 10000
mid_tax_amt = 20000

if income <= no_tax_amt:
    tax = 0
elif mid_tax_amt >= income > no_tax_amt:
    tax = rate_for_mid_bracket * (income - no_tax_amt)
else:
    tax = rate_for_top_bracket * (income - mid_tax_amt) + rate_for_mid_bracket * no_tax_amt

print("Total tax to pay is USD", round(tax, 2))
