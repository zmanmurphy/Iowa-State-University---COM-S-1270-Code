# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This code will print out a right triangle made of one '1' in the first row, two '2's in the second roaw, and so on.

def sameNumberTriangle(num):
    for i in range(num + 1):
        for j in range(1, i + 1):
            print(i, end = " ")
        print()

def main():
    num = 5
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()