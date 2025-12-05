# Zachary Murphy             10-16-25
# Lab #7 Section F

# This code will find the maximum and minimum values in a user generated list of numbers.

def takeInput():
    numList = []
    running = True
    while running:
        numAdd = str(input("Add a number to your list. Enter '*' if you've finished your list. "))
        if numAdd == "*":
            running = False
        else:
            numList.append(numAdd)
    return numList

def findMin(x):
    firstMin = x[0]
    for i in range(1, len(x)):
        b = x[i]
        if firstMin > b:
            firstMin = b
    return firstMin

def findMax(y):
    firstMax = y[0]
    for i in range(1, len(y)):
        c = y[i]
        if firstMax < c:
            firstMax = c
    return firstMax

def main():
    numList = takeInput()
    newList = []
    for i in range(0, len(numList)):
        a = int(numList[i])
        newList.append(a)
    min = findMin(newList)
    print(f"The minimum value in the list is {min}")
    max = findMax(newList)
    print(f"The maximum value in this list is {max}")

if __name__ == "__main__":
    main()