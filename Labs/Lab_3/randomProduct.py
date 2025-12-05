# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Gives a random product using "a" number of integers between "b" and "c+1".

import random

def random_Product (a, b, c):
    val = 1
    for i in range(a):
        val1 = random.randint(b, c)
        val = val1 * val
    return val

def main():
    a = int(input("Please Enter an Integer: "))
    b = int(input("Please Enter an Integer: "))
    c = int(input("Please Enter an Integer Greater Than the Last One Entered: "))
    answer = random_Product(a, b, c)
    print(f"Your random number is {answer}")

if __name__ == "__main__":
    main()