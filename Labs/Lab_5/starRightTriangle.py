# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This Code will draw a right triangle made of stars with as many rows as the user so wishes.

def starRightTriangle(num):
    for i in range(num + 1):
        print("*" * i)


def main():
    num = int(input(print("Please Enter the number of rows you want in the right triangle: ")))
    starRightTriangle(num)

if __name__ == "__main__":
    main()