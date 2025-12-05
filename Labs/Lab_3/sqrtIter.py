# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code will calculate the squareroot of any number as many iterations as the user wants.

# URL: https://www.cuemath.com/algebra/square-root-of-2/
# Date Accessed: 9-18-25

def sqrtIter(x, iterations):
    y = (x + 1) / 2
    for i in range(iterations):
        y = ((x/y) + y) / 2
    return y

def main():
    x = int(input("Please Enter and Integer: "))
    iterations = int(input("Please Enter the amount of iterations: "))
    answer = sqrtIter(x, iterations)
    print(f"The answer is {answer}")

if __name__ == "__main__":
    main()
    