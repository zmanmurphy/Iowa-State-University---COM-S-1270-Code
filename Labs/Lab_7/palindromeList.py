# Zachary Murphy             10-16-25
# Lab #7 Section F

# This code will take a user generated list of words, and then determine which words within the list are palindromes.

def palindromeList(palList):
    for i in range(0, len(palList)):
        if palList[i] == palList[-(i+1)]:
            answer = True
        else:
            answer = False
            break
    return answer
    
def takeInput():
    numList = []
    running = True
    while running:
        numAdd = str(input("Add a word to your list. Enter '*' if you've finished your list. "))
        if numAdd == "*":
            running = False
        else:
            numList.append(numAdd)
    return numList

def main():
    list1 = takeInput()
    answer = palindromeList(list1)
    print(f"{answer}")

if __name__ == "__main__":
    main()