# Zachary Murphy             9-26-25
# Assignment #2
#
# This code will allow the user to input two integers, and do one of seven different operations with them.
# It will additionally allow the user to get a random(lucky) number.

import random

print("Lucky Calculator!")
print("By: Zach Murphy")
print("COM S 1270 4")

print("What would you like to do?")
choice = input(print("[c]alculator, [l]ucky number, [q]uit?"))
if choice == "c":
    num1 = float(input(print("Pick your first number: ")))
    num2 = float(input(print("Pick your second number: ")))
    operation = input(print("Pick the operation you want. Your choices are, [+], [-], [*], [/], [//], [%], [**], [q]uit. "))
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    elif operation == "//":
        answer = num1 // num2
    elif operation == "%":
        answer = num1 % num2
    elif operation == "**":
        answer = num1 ** num2
    elif operation == "q":
        print("Goodbye!")
    else:
        print("Please Enter an Operation.")
    print (f"The answer is {answer}.")

elif choice == "l":
    min = int(input(print("Please Enter the Minimum of your Lucky Number Range: ")))
    max = int(input(print("Please Enter the Maximum of your Lucky Number Range: ")))
    luckyNum = random.randint(min, max)
    print(f"Your Lucky Number is {luckyNum}.")

elif choice == "q":
    print("Goodbye!")

else:
    print("Please Enter an Appropriate Input.")


