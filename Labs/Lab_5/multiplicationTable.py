# Zachary Murphy             10-2-2025
# Lab #5 - Section F
# This code will utilize nested for loops to create the multiplication table up to 10.


def multiplicationTable(lowNum, highNum):
    for i in range(lowNum, highNum+1):
        for j in range(lowNum, highNum + 1):
            x = i * j
            print(x, end=" ")
        print()

def main():
    lowNum = 1
    highNum = 10
    multiplicationTable(lowNum, highNum)


if __name__ == "__main__":
    main()