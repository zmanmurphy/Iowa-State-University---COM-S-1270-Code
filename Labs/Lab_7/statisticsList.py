# Zachary Murphy             10-16-25
# Lab #7 Section F

# This code will generate a large list with values ranging from 1 to 2000, and then calculate the mean and median of the list.

import random

def findMean(list):
    # A mean is the average of all values in a set.
    # URL: https://byjus.com/maths/mean/
    # Accessed: 10-16-25
    listTotal = 0
    for i in range(0, len(list)):
        listTotal = listTotal + list[i]
    mean = listTotal/len(list)
    return mean

def findMedian(list):
    # A median is the middle value of a sorted set of values, not to be confused with the average value.
    # URL: https://byjus.com/maths/median-definition/
    # Accessed: 10-16-25
    list.sort()
    if len(list) % 2 == 0:
        print(len(list))
        a = list[int(len(list) / 2)]
        b = list[int((len(list) / 2) + 1)]
        median = (a+b) / 2
    else:
        c = int((len(list) / 2) + 0.5)
        median = list[c]
    return median


def generateInput():
    x = random.randint(200, 500)
    list = []
    for i in range(0, x):
        y = random.randint(1, 2000)
        list.append(y)
    return list

def main():
    list = generateInput()
    mean = findMean(list)
    median = findMedian(list)
    print(f"The mean of the generated list is {mean}")
    print(f"The median of the generated list is {median}")


if __name__ == "__main__":
    main()