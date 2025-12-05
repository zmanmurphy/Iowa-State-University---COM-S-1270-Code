# Zachary Murphy             10-30-25
# Lab #8 Section F

# This code will take a file as a user input, and then create a new file that has each word and how many times that word is used in the original file.

def analyzeBook(fileName):
    with open(fileName + '.txt', 'r', encoding = 'utf-8') as f:

        count = {}

        for line in f:
            for word in line.split():

                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
        
                # ignore case
                word = word.lower()

                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def outputAnalysis(fileName, countDic):
    keys = list(countDic.keys())
    keys.sort()

    # save the word count analysis to a file
    with open(fileName + '_analysis.txt', 'w', encoding = 'utf-8') as out:
        for word in keys:
            out.write(word + " " + str(countDic[word]))
            out.write('\n')

def main():
    fileName = str(input("Enter the file name exluding .txt: "))
    countDic = analyzeBook(fileName)
    outputAnalysis(fileName, countDic)

if __name__ == "__main__":
    main()