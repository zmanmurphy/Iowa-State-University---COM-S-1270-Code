# Zachary Murphy             10-17-25
# Lab #7 Section F

# This code will take a user generated list and a desired number of rotations either left or right, and it will rotate the values in the list by the number of times desired and in the desired direction

def takeInput():
    numList = []
    running = True
    while running:
        numAdd = str(input("Add a number to your list. Enter '*' if you've finished your list. "))
        if numAdd == "*":
            running = False
        else:
            numAdd = int(numAdd)
            numList.append(numAdd)
    return numList

def rotateList(numList, numRot):
    if numRot == 0:
        pass
    elif numRot/abs(numRot) > 0:
        for i in range(0, numRot):
            a = numList[len(numList) - 1]
            del numList[len(numList) - 1]
            numList.insert(0, a)
    elif numRot/abs(numRot) < 0:
        for i in range(0, abs(numRot)):
            a = numList[0]
            del numList[0]
            numList.append(a)
    return numList

def main():
    numList = takeInput()
    numRot = int(input("Enter the desired number of rotations and desired direction. Negative rotates left, and positive rotates right."))
    newList = rotateList(numList, numRot)
    print(newList)

if __name__ == "__main__":
    main()