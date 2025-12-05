# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the Circumference of a Circle using functions.

import math

def circumference(radius):
    # Definition = The measurement of the boundary of a circle.
    # CITATION - https://byjus.com/maths/circumference-of-a-circle/
    # CITATION - Date Accessed: 9-11-25

    return 2 * math.pi * radius

def main():
    radius = int(input("Please Enter the Radius: "))
    answer = circumference(radius)
    print(f"The circumference is {answer}")

if __name__ == "__main__":
    main()