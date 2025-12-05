# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This code will print out a pyramid that starts with 1 at its peak, and has 1-5 at it's base.

def numberPyramid(num):
    for i in range(1, num + 1):
        print(" " * (5 - i), end = " ")
        for j in range(1, i + 1):
            print(j, end = " ")
        print()

def main():
    num = 5
    numberPyramid(num)

if __name__ == "__main__":
    main()