# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the Area of a Circle using functions.

import math
def area (radius):
    # Definition = The region occupied by a circle in a two-dimensional plane.
    # CITATION - https://byjus.com/maths/area-of-circle/
    # CITATION - Date Accessed: 9-11-25

    return math.pi * (radius ** 2)

def main():
    radius = int(input("Please Enter the Radius: "))
    answer = area(radius)
    print(f"The Area is {answer}")

if __name__ == "__main__":
    main()