# Zachary Murphy             10/9/25
# Lab #6 Section F
# This code will check if a string contains a certain substring.

def findSubStringV1(a):
    c = a.find("cat")
    return c

def findSubStringV2(b):
    if "cat" in b:
        d = b.index("cat",0,len(b))
    else:
        d = -1
    return d

def findSubStringV3(e):
    for i in range(len(e)):
        if "c" == e[i]:
            if "a" == e[i+1]:
                if "t" == e[i+2]:
                    k = i
                    break
            else:
                k = -1
        else: k = -1
    return k

def main():
    a = str(input("Enter a phrase/word. "))
    findSubStringV1(a)
    print(f"Index is {findSubStringV1(a)}")
    print("-------------------------")
    b = str(input("Enter another phrase/word. "))
    findSubStringV2(b)
    print(f"Index is {findSubStringV2(b)}")
    print("-------------------------")
    e = str(input("Enter another phrase/word. "))
    findSubStringV3(e)
    print(f"Index is {findSubStringV3(e)}")

if __name__ == "__main__":
    main()