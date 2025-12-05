# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the Annual Percentage Rate.

# Definition = The cost you pay each year for borrowing the money, including fees that you have to pay to get the loan, expressed as a percentage.
# CITATION - https://ask.fdic.gov/fdicinformationandsupportcenter/s/article/Q-What-is-annual-percentage-rate-APR?language=en_US
# CITATION - Date Accessed: 9-11-25

interest_charges = int(input("Please Enter the interest charges: "))
fees = int(input("Please Enter the initial fees: "))
loan_amount = int(input("Please Enter the loan amount: "))
days_in_term = int(input("Please Enter the number of days in the term: "))

apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100

print(f"The Annual Percentage Rate is {apr}")