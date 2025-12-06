# Zachary Murphy             12-6-25
# Lab #11 Section F

# This code will provide two different functions that can tell if a string is a palindrome or not, and then output True if it is and False if it isn't.

def isPalindromeIterative(s):
    reverse = ""
    for i in "!?.,:;[]`'":
        for ch in range(len(s)):
            if ch > len(s) - 1:
                break
            if i == s[ch]:
                s = s[:ch] + s[ch+1:]
    s = s.lower()

    for k in range(len(s)):
        reverse = reverse + s[(-k) - 1]
    
    if reverse == s:
        return True
    else:
        return False

def isPalindromeRecursive(s, cond):
    s = s.lower()
    
    if s == "" or cond == False:
        return s, cond

    if cond == False:
        cond = False
    
    elif s[0] == s[len(s)-1]:
        s = s[1:len(s)-1]
    
    else:
        cond = False

    return isPalindromeRecursive(s, cond)


def main():
    s = str(input("Enter a string: "))
    print(isPalindromeIterative(s))
    s, cond = isPalindromeRecursive(s, True)
    print(cond)

if __name__ == "__main__":
    main()