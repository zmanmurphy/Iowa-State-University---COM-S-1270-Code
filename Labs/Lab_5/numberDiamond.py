# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This code will print out a number diamond that has 1 at both of its peaks and 1-5 in the middle.

def numberDiamond(num):
    for i in range(1, num + 1):
        print(" " * (5 - i), end = " ")
        for j in range(1, i + 1):
            print(j, end = " ")
        print()
    if i == 5:
        for k in range(4, 0, -1):
            print(" " * (5 - k), end = " ")
            for l in range(1, k + 1):
                print(l, end = " ")
            print()

def main():
    num = 5
    numberDiamond(num)

if __name__ == "__main__":
    main()