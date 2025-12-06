# Zachary Murphy             12-5-25
# Lab #11 Section F

# This code will have multiple solutions to the Two-Sum problem.
# URL: https://interviewing.io/questions/two-sum
# Accessed: 12-5-25
# First two functions come from the article.

def twoSumLoops(list1, target):
    for i in range(len(list1)-1):
        for k in range(i, len(list1)-1):
            if list1[i] + list1[k] == target:
                return [i, k]
    return "No two values add to target value."
    
def twoSumDict(list1, target):
    numToIndex = {}

    for i in range(len(list1)):
        complement = target - list1[i]

        if complement in numToIndex:
            return [numToIndex[complement], i]
        
        numToIndex[list1[i]] = i
    return "No two values add to target value."

def twoSumLoopsAll(list1, target):
    indicesList = []
    addList = []
    for i in range(len(list1)-1):
        for k in range(i, len(list1)-1):
            if list1[i] + list1[k] == target:
                addList = [i, k]
                indicesList.append(addList)
    if indicesList == []:
        return "No two values add to target value."
    else:
        return indicesList

def twoSumDictAll(list1, target):
    numToIndex = {}
    indicesList = []
    addList =[]

    for i in range(len(list1)):
        complement = target - list1[i]

        if complement in numToIndex:
            addList = [numToIndex[complement], i]
            indicesList.append(addList)
        
        if list1[i] + list1[i] == target:
            addList = [i, i]
            indicesList.append(addList)

        numToIndex[list1[i]] = i
    if indicesList == []:
        return "No two values add to target value."
    else:
        return indicesList

def main():
    list1 = [1,2,3,4,5,6,7]
    target = 6
    print(twoSumLoops(list1, target))
    print(twoSumDict(list1, target))
    print(twoSumLoopsAll(list1, target))
    print(twoSumDictAll(list1, target))


if __name__ == "__main__":
    main()