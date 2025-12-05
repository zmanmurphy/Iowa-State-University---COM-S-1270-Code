# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This code will print out a student loan amortization based on user inputed values.

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    numberOfPayments = numberOfYears * 12
    loanAmount = principal
    print("Period   Total Payment Due   Computed Interest   Principal Due   Principal Balance")
    for i in range(1, numberOfPayments + 1):
        monthlyInterestRate = (yearlyInterestRate/100)/12
        tmp = loanAmount * ((monthlyInterestRate * ((1 + monthlyInterestRate)**numberOfPayments))/(((1 + monthlyInterestRate)**numberOfPayments) - 1))
        principalDue = tmp - (principal * (monthlyInterestRate))
        monthlyInterestPayment = tmp - principalDue
        principal = principal - principalDue
        tmp = round(tmp, 2)
        monthlyInterestPayment = round(monthlyInterestPayment, 2)
        principalDue = round(principalDue, 2)
        principal2 = round(principal, 2)
        print(f"{i}        {tmp}              {monthlyInterestPayment}               {principalDue}           {principal2}")

def main():
    principal = float(input("Please Enter the Principal: "))
    yearlyInterestRate = float(input("Please Enter the Yearly Interest Rate: "))
    numberOfYears = int(input("Please Enter the Number of Years: "))
    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)

if __name__ == "__main__":
    main()