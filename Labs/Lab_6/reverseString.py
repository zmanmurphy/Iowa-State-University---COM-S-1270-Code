# Zachary Murphy             10/9/25
# Lab #6 Section F
# This code will reverse whatever text is inputed by the user.

def reverseStringV1(a):
    str1 = a[-1:(len(a)+1)*-len(a):-1]
    return str1

def reverseStringV2(b):
    str2 = reversed(b)
    str2V2 = ("").join(str2)
    return str2V2

def reverseStringV3(c):
    x = -1
    str3 = []
    for i in range(len(c)-1, -1, -1):
        str3.append(c[x])
        x = x - 1
    str3V2 = ("").join(str3)
    return str3V2

def reverseStringV4(d):
    str4 = []
    x = -1
    for i in d:
        str4.append(d[x])
        x = x - 1
    return ("").join(str4)

def reverseStringV5(e):
    y = True
    t = - 1
    str5 = []
    while y:
        str5.append(e[t])
        t = t - 1
        if -(len(e) + 1) == t:
            y = False
    return ("").join(str5)         

def main():
    a = str(input("Enter the phrase you would like to reverse. "))
    reverseStringV1(a)
    print(reverseStringV1(a))
    print("-----------------------")
    b = str(input("Enter another phrase you would like reversed. "))
    reverseStringV2(b)
    print(reverseStringV2(b))
    print("-----------------------")
    c = str(input("Enter another phrase you want reversed. "))
    reverseStringV3(c)
    print(reverseStringV3(c))
    print("-----------------------")
    d = str(input("Enter another phrase you want reversed. "))
    reverseStringV4(d)
    print(reverseStringV4(d))
    print("-----------------------")
    e = str(input("Enter another string you want reversed. "))
    reverseStringV5(e)
    print(reverseStringV5(e))


if __name__ == "__main__":
    main()