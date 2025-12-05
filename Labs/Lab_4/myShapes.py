# Zachary Murphy             9-25-25
# Lab #4 Section F - This Code Calculates the area and perimeters of circles and rectangles.

import math
def areaCircle(radius):
    return math.pi * (radius ** 2)

def areaCircleCall():
    radius = int(input("Please Enter the Radius: "))
    answer = areaCircle(radius)
    print(f"The Area is {answer}")

#------------------------------------------------

def area(l, w):
    return l * w

def areaCall():
    l = int(input("Please Enter the Length: "))
    w = int(input("Please Enter the Width: "))
    answer = area(l, w)
    print(f"Area of Rectangle is {answer}")

#-------------------------------------------------

def perimeter(l, w):
    return 2 * (l + w)

def perimeterCall():
    l = int(input("Please Enter the Rectangle's Length: "))
    w = int(input("Please Enter the Rectangle's Width: "))
    answer = perimeter(l, w)
    print(f"The Perimeter of the rectangle is {answer}")

#--------------------------------------------------

def circumference(radius):
    return 2 * math.pi * radius

def circumferenceCall():
    radius = int(input("Please Enter the Radius: "))
    answer = circumference(radius)
    print(f"The circumference is {answer}")