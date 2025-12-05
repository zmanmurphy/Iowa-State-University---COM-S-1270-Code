# Zachary Murphy             10/9/25
# Lab #6 Section F
# This code will check if a phrase/word is a palindrome.

import reverseString

def palindromeCheckV1(a):
    check = reverseString.reverseStringV1(a)
    if a == check:
        return True
    else:
        return False

def palindromeCheckV2(b):
    t = 0
    for i in range(len(b)):
        if b[t] == b[-(t+1)]:
            p = True
        else:
            p = False
            break
        t += 1
    return p

def main():
    a = str(input("Enter a word or phrase you want checked. "))
    palindromeCheckV1(a)
    if palindromeCheckV1(a):
        print(f"{a} is a palindrome.")
    else:
        print(f"{a} isn't a palindrome.")
    print("----------------------")
    b = str(input("Enter another word or phrase you want checked. "))
    palindromeCheckV2(b)
    if palindromeCheckV2(b):
        print(f"{b} is a palindrome.")
    else:
        print(f"{b} isn't a palindrome.")


if __name__ == "__main__":
    main()