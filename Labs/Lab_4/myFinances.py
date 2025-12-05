# Zachary Murphy             9-25-25
# Lab #4 Section F - This Code Calculates the Annual Percentage Rate and Compound Amount.

def apr(interest_charges, fees, loan_amount, days_in_term):
    return (((interest_charges + fees) / loan_amount) / days_in_term) * 100

def aprCall():
    interest_charges = int(input("Please Enter the interest charges: "))
    fees = int(input("Please Enter the initial fees: "))
    loan_amount = int(input("Please Enter the loan amount: "))
    days_in_term = int(input("Please Enter the number of days in the term: "))
    answer = apr(interest_charges, fees, loan_amount, days_in_term)
    print(f"The Annual Percentage Rate is {answer}")

#---------------------------------------------------------------------------------

def accured_amount(principal, rate, number_compounds, time):
    return principal * (1 + (rate/100) / number_compounds)**(number_compounds * time)

def accrued_amountCall():
    principal = int(input("Please Enter the Principal: "))
    rate = float(input("Please Enter the rate of interest in a decimal: "))
    number_compounds = int(input("Please Enter the number of compounds per year: "))
    time = int(input("Please Enter the time in years: "))
    answer = accured_amount(principal, rate, number_compounds, time)
    print(f"The total compounded amount is ${answer}")