# Zachary Murphy             12-6-25
# Lab #11 Section F

# This code will have two solutions to the fizzbuzz game.
# URL: https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
# Accessed: 12-6-25
# Bulk of this code is from the article.

def fizzBuzzModulus(num):
    output = []

    for i in range(1, num + 1):
        if i % 7 == 0 and i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzzBazz")

        elif i % 7 == 0 and i % 3 == 0:
            output.append("FizzBazz")

        elif i % 7 == 0 and i % 5 == 0:
            output.append("BuzzBazz")

        elif i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")

        elif i % 3 == 0:
            output.append("Fizz")

        elif i % 5 == 0:
            output.append("Buzz")

        elif i % 7 == 0:
            output.append("Bazz")
        
        else:
            output.append(str(i))

    return output

def fizzBuzzDict(num):
    output = []
    fizzCount = 0
    buzzCount = 0
    bazzCount = 0
    for i in range(1, num + 1):
        fizzCount += 1
        buzzCount += 1
        bazzCount += 1

        if fizzCount == 3 and buzzCount == 5 and bazzCount == 7:
            output.append("FizzBuzzBazz")
            fizzCount = 0
            buzzCount = 0
            bazzCount = 0

        elif fizzCount == 3 and buzzCount == 5:
            output.append("FizzBuzz")
            fizzCount = 0
            buzzCount = 0

        elif buzzCount == 5 and bazzCount == 7:
            output.append("BuzzBazz")
            buzzCount = 0
            bazzCount = 0

        elif fizzCount == 3 and bazzCount == 7:
            output.append("FizzBazz")
            fizzCount = 0
            bazzCount = 0

        elif fizzCount == 3:
            output.append("Fizz")
            fizzCount = 0

        elif buzzCount == 5:
            output.append("Buzz")
            buzzCount = 0

        elif bazzCount == 7:
            output.append("Bazz")
            bazzCount = 0

        else:
            output.append(str(i))
    return output

def main():
    num = int(input("Enter an integer: "))
    print(fizzBuzzModulus(num))
    print(fizzBuzzDict(num))

if __name__ == "__main__":
    main()