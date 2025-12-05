# Zachary Murphy             9-25-25
# Lab #4 Section F - This Code will Utilize the Turtle module to draw a tridecagon using loops and functions.

import turtle

def drawMultipleTridecagons(s, x, y, t, nr, sr):
    screen = turtle.Screen()
    for i in range(nr):
        tridecagonTurtle(s, x, y, t)
        x = x + sr
    screen.exitonclick()

def tridecagonTurtle(s, x, y, t):
    t.teleport(x, y)
    for i in range(13):
        t.right(27.69)
        t.forward(s)
    
def main():
    s = int(input("Please Enter the Length of the Sides: "))
    x = int(input("Please Enter the Starting X-Value: "))
    y = int(input("Please Enter the Starting Y-Value: "))
    nr = int(input("Please Enter the Number of Times you want to Draw a Tridecagon: "))
    sr = int(input("Please Enter the Amount of Space you Want between each Tridecagon: "))
    t = turtle.Turtle()
    drawMultipleTridecagons(s, x, y, t, nr, sr)

if __name__ == "__main__":
    main()