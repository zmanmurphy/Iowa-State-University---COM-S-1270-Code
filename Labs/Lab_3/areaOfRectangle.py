# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the Area of a Rectangle using functions.

def area (l, w):
    # Definition = The region covered by a rectangle in a two-dimensional plane.
    # CITATION - https://byjus.com/maths/area-of-rectangle/
    # CITATION - Date Accessed: 9-11-25

    return l * w

def main():
    l = int(input("Please Enter the Length: "))
    w = int(input("Please Enter the Width: "))
    answer = area(l, w)
    print(f"Area of Rectangle is {answer}")

if __name__ == "__main__":
    main()