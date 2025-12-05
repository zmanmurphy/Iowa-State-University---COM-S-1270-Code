# Zachary Murphy             10-31-25
# Lab #8 Section F

# This code will take one file of student's id's and names, and one file of the students homework and the grades they recieved on them. It will then create a new file that has the student's names, id's, total scores, sum of scores, and average scores.

def getFile():
    fileName = str(input("Enter the file's name excluding .txt: "))
    with open(fileName + '.txt', 'r', encoding = 'utf-8') as f:
        contents = f.read().splitlines()
    return contents

def createLists(contents):
    originalList = []
    idList = []
    nameList = []
    for i in range(1, len(contents)):
        id = ""
        name = ""
        for j in contents[i]:
            if ord(j) > 47 and ord(j) < 58:
                id += j
            elif ord(j) > 64 and ord(j) < 91:
                name = name + " " + j
            elif ord(j) > 96 and ord(j) < 123:
                name += j
        idList.append(id)
        nameList.append(name)
    for i in range(len(nameList)):
        nameList[i] = nameList[i].strip()
    originalList.append(idList)
    originalList.append(nameList)
    return originalList
                
def splitContents2(contents2, originalList):
    idList = originalList[0]
    totalAssignmentsList = []
    for i in range(1, len(contents2)):
        idNum = ""
        breakNum = False
        for char in contents2[i]:
            idNum += char
            for j in range(len(idList)):
                if idNum == idList[j]:
                    totalAssignmentsList.append(idNum)
                    breakNum = True
                    break
            if breakNum:
                break
    return totalAssignmentsList
        
def getIDAssignmentTotals(totalAssignmentsList, originalList):
    idAssignmentsTotals = []
    idList = originalList[0]
    for k in range(len(idList)):
        idAssignmentsTotals.append(0)
    for i in range(len(totalAssignmentsList)):
        for j in range(len(idList)):
            if totalAssignmentsList[i] == idList[j]:
                idAssignmentsTotals[j] = idAssignmentsTotals[j] + 1
                break
    originalList.append(idAssignmentsTotals)
    return originalList

def sumScores(contents2, newList):
    idAssignmentsTotals = newList[2]
    sumsList = []
    for i in range(len(idAssignmentsTotals)):
        sumsList.append(0)
    for k in range(1, len(contents2)):
        idNum = ""
        j = 0
        for char in contents2[k]:
            if j > 15:
                if ord(char) > 47 and ord(char) < 58:
                    idNum += char
            j += 1
        p = 0
        for l in range(len(idAssignmentsTotals)):
            if k < 1 + idAssignmentsTotals[l] + p:
                sumsList[l] += int(idNum)
                break
            p += idAssignmentsTotals[l]
    newList.append(sumsList)
    return newList

def averageScores(newerList):
    averageScoresList = []
    totalAssignmentsList = newerList[2]
    sumsList = newerList[3]
    for i in range(len(sumsList)):
        averageScore = sumsList[i] / totalAssignmentsList[i]
        averageScoresList.append(averageScore)
    newerList.append(averageScoresList)
    return newerList
    
def createFinalFile(finalList):
    totalAssignmentsList = finalList[2]
    sumsList = finalList[3]
    averagesList = finalList[4]
    nameList = finalList[1]
    idList = finalList[0]
    with open('grades.txt', 'w', encoding = 'utf-8') as f:
        f.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average\n")
        for i in range(len(finalList) - 1):
            for k in range(len(finalList)):
                if k < 4:
                    f.write(str(finalList[k][i]) + ",")
                elif k == 4 and i != 3:
                    f.write(str(finalList[k][i]) + "\n")
                else:
                     f.write(str(finalList[k][i]))


def main():
    contents = getFile()
    originalList = createLists(contents)
    contents2 = getFile()
    totalAssignmentsList = splitContents2(contents2, originalList)
    newList = getIDAssignmentTotals(totalAssignmentsList, originalList)
    newerList = sumScores(contents2, newList)
    finalList = averageScores(newerList)
    createFinalFile(finalList)

if __name__ == "__main__":
    main()