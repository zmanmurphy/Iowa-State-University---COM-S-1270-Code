# Zachary Murphy             10/10/25
# Lab #6 Section F
# This code will create a pattern using the turtle module and a set of rules.
# 
# URL: https://runestone.academy/ns/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html?mode=browsing
# Author: Brad Miller, David Ranum
# Accessed: 10/10/25

import turtle
import random

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-T++F-P'   # Rule 1
    elif ch == 'T':
        newstr = 'F+P--F'
    elif ch == 'P':
        newstr = 'T+-P-F'
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "T":
            tridecagonTurtle(aTurtle)
        elif cmd == "P":
            aTurtle.teleport(random.randint(-200, 200), random.randint(-150, 150))


def tridecagonTurtle(t):
    for i in range(13):
        t.right(27.69)
        t.forward(30)

def main():
    inst = createLSystem(4, "F")  
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    drawLsystem(t, inst, 60, 30)
    wn.exitonclick()
    

if __name__ == "__main__":
    main()