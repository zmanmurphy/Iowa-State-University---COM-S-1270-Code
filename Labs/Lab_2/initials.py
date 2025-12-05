# Zachary Murphy             9-11-25
# Drawing the Initials of My Name Using Turtle

import turtle

screen = turtle.Screen()
john = turtle.Turtle()

screen.bgcolor("blue")
john.color("orange")
john.pensize(7)
john.fillcolor("green")

john.begin_fill()
john.teleport(-300, 250)

john.forward(175)

john.right(135)
john.forward(255)

john.left(45)
john.forward(50)

john.left(90)
john.forward(225)

john.left(90)
john.forward(50)

john.left(90)
john.forward(175)

john.right(135)
john.forward(255)

john.left(45)
john.forward(50)

john.left(90)
john.forward(225)

john.left(90)
john.forward(50)

john.end_fill()

# start of letter M

john.teleport(0, 300)
john.begin_fill()

john.forward(285)

john.left(90)
john.forward(50)

john.left(90)
john.forward(245)

john.right(165)
john.forward(260)

john.left(75)
john.forward(50)

john.left(75)
john.forward(260)

john.right(165)
john.forward(245)

john.left(90)
john.forward(50)

john.left(90)
john.forward(285)

john.left(90)
john.forward(75)

john.left(75)
john.forward(260)

john.right(150)
john.forward(260)

john.left(75)
john.forward(75)

john.end_fill()

screen.exitonclick()