# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code will Evaluate the Perimeter of a Rectangle using functions.

def perimeter(l, w):
    # Definition = The total distance covered by the rectangle around its outside.
    # CITATION - https://byjus.com/maths/perimeter-of-rectangle/
    # CITATION - Date Accessed: 9-11-25

    return 2 * (l + w)

def main():
    l = int(input("Please Enter the Rectangle's Length: "))
    w = int(input("Please Enter the Rectangle's Width: "))
    answer = perimeter(l, w)
    print(f"The Perimeter of the rectangle is {answer}")

if __name__ == "__main__":
    main()