# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the compound amount of a loan/savings account after accruing interest on interest using functions.

def accured_amount(principal, rate, number_compounds, time):
    # Definition = The interest calculated on the principal and the interest accumulated over the previous period.
    # CITATION - https://byjus.com/maths/compound-interest/
    # CITATION - Date Accessed: 9-11-25

    return principal * (1 + (rate/100) / number_compounds)**(number_compounds
    * time)

def main():
    principal = int(input("Please Enter the Principal: "))
    rate = float(input("Please Enter the rate of interest in a decimal: "))
    number_compounds = int(input("Please Enter the number of compounds per year: "))
    time = int(input("Please Enter the time in years: "))
    answer = accured_amount(principal, rate, number_compounds, time)
    print(f"The total compounded amount is ${answer}")

if __name__ == "__main__":
    main()