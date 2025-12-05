# Zachary Murphy             10-17-25
# Lab #7 Section F

# This code will take a user generated list and individual number. It will then scan the list and move all values equal to the individial number to the end of the list.

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

def endNum(numList, num):
    running2 = True
    t = 0
    while running2:
        for i in range(0, len(numList)):
            if numList[i] == num:
                del numList[i]
                numList.append(num)
        t += 1
        if t == len(numList):
            running2 = False
    return numList
        
def main():
    numList = takeInput()
    num = int(input("Enter the number you would like to move to the end of the list. "))
    newList = endNum(numList, num)
    print(newList)


if __name__ == "__main__":
    main()