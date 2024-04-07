"""Tutorial of how to use turtle drawing for EX08."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

side_length: int = 300

# moving the starting position
leo.penup()
leo.goto(-150, 90)
leo.pendown()
leo.color("green", "pink")
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 4):
    leo.forward(side_length)
    leo.right(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.penup()
bob.goto(-150, 90)
bob.pendown()
bob.color('dark blue')
bob.speed(70)

i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.right(121)
    i += 1
    side_length *= .97
done()