# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code will Utilize the Turtle module to draw a tridecagon using loops and functions.

# URL: https://testbook.com/maths/tridecagon
# Date Accessed: 9-18-25

import turtle

def tridecagonTurtle(s, x, y, t):
    screen = turtle.Screen()
    t.teleport(x, y)
    for i in range(13):
        t.right(27.69)
        t.forward(s)
    screen.exitonclick()
    
def main():
    s = int(input("Please Enter the Length of the Sides: "))
    x = int(input("Please Enter the Starting X-Value: "))
    y = int(input("Please Enter the Starting Y-Value: "))
    t = turtle.Turtle()
    tridecagonTurtle(s, x, y, t)

if __name__ == "__main__":
    main()