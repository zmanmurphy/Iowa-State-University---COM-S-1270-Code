# Zachary Murphy             9-25-25
# Lab #4 Section F - This Code will figure out if a user-inputed year is a leap year or not.

def findLeapYear(year):
    answer = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                answer = True
            else:
                answer = False
        else:
            answer = True
    if answer == True:
        answer = "is"
    elif answer == False:
        answer = "isn't"
    return answer

def main():
    year = int(input("Please Enter a Year: "))
    answer = findLeapYear(year)
    print(f"The year {year} {answer} a leap year.")

if __name__ == "__main__":
    main()