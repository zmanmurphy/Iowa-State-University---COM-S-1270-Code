# Zachary Murphy             11-1-25
# Lab #8 Section F

# This code will a user inputed sentence, and then swap each unique word with a different word. All iterations of each unique word will swap to the same word. Then the program will spit the new sentence back out.

import random

def getSentence():
    originalString = str(input("Enter a sentence: "))
    wordList = originalString.split()
    return wordList

def createDict(wordList):
    valueList = []
    newDict = {}
    for i in range(len(wordList)):
        valueList.append(random.randint(0, len(wordList) - 1))
    for k in range(len(valueList)):
        if k == 0:
            newDict[wordList[k]] = wordList[valueList[k]]
        else:
            for keys in newDict:
                if wordList[k] == keys:
                    break
                else:
                    newDict[wordList[k]] = wordList[valueList[k]]
                    break
    return newDict

def createNewString(newDict, wordList):
    newList = []
    newString = ""
    for i in range(len(wordList)):
        for k in newDict:
            if wordList[i] == k:
                newList.append(newDict[k])
                break
    for p in range(len(newList)):
        if p < len(newList) - 1:
            newString += newList[p] + " "
        else:
            newString += newList[p]
    return newString

def main():
    wordList = getSentence()
    print(wordList)
    print("-----------------------------")
    newDict = createDict(wordList)
    print(newDict)
    print("-----------------------------")
    newString = createNewString(newDict, wordList)
    print(newString)

if __name__ == "__main__":
    main()