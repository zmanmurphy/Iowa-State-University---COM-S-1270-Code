# Zachary Murphy             10-30-25
# Lab #8 Section F

# This code will take a file as an input and remove all characters that aren't ASCII characters, and then make a new file with the remaining characters.

def getFile(fileName):
    with open(fileName + '.txt', 'r', encoding = 'utf-8') as f:
        contents = f.read()
    return contents

def removeNonASCII(string):
    cleanString = ""
    for char in string:
        if ord(char) < 128:
            cleanString += char
    return cleanString

def createNewFile(fileName, newContents):
    with open(fileName + '_clean.txt', 'w', encoding = 'utf-8') as h:
        h.write(newContents)

def main():
    fileName = str(input("Enter the file name excluding the .txt: "))
    contents = getFile(fileName)
    newContents = removeNonASCII(contents)
    createNewFile(fileName, newContents)

if __name__ == "__main__":
    main()