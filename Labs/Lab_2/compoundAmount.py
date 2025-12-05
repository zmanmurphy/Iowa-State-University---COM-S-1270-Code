# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the compound amount of a loan/savings account after accruing interest on interest.

# Definition = The interest calculated on the principal and the interest accumulated over the previous period.
# CITATION - https://byjus.com/maths/compound-interest/
# CITATION - Date Accessed: 9-11-25

principal = int(input("Please Enter the Principal: "))
rate = float(input("Please Enter the rate of interest in a decimal: "))
number_compounds = int(input("Please Enter the number of compounds per year: "))
time = int(input("Please Enter the time in years: "))

accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds
* time)

print(f"The total compounded amount is ${accrued_amount}")