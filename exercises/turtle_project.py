"""Draws a Christmas tree scene. For the extra five points I used random.randint() to vary the size and color of the ornaments on the tree."""
__author__ = "730469865"


from turtle import Turtle, colormode, done, tracer, update
colormode(255)
import random


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    update()
    # draw the tree
    tree: Turtle = Turtle()
    tree.speed(0)
    draw_triangle(tree, -7, 290, 150, 212)
    draw_triangle(tree, -25, 260, 240, 300)
    draw_triangle(tree, -29, 200, 300, 370)
    draw_triangle(tree, -63, 155, 390, 430)
    draw_triangle(tree, -70, 90, 450, 500)
    # draw the ornaments 
    balls: Turtle = Turtle()
    balls.speed(0)
    x = range(5)
    for n in x: # upper level
        draw_circle(balls, random.randint(-40, 30), random.randint(180, 230), random.randint(5,10))
    x = range(8)
    for n in x: # second level
        draw_circle(balls, random.randint(-60, 70), random.randint(100, 180), random.randint(5,10))
    x = range(10)
    for n in x: # third level
        draw_circle(balls, random.randint(-100, 90), random.randint(0, 100), random.randint(5, 10))
    x = range(12)
    for n in x: # fourth level
        draw_circle(balls, random.randint(-140, 130), random.randint(-120, 0), random.randint(5, 10))
    x = range(12)
    for n in x: # fifth level
        draw_circle(balls, random.randint(-165, 175), random.randint(-220, -120), random.randint(5, 10))
    # draw the presents and tree stump
    box: Turtle = Turtle()
    box.speed(0)
    star: Turtle = Turtle()
    star.speed(0)
    draw_square(box, -180, -200, 90, "red")
    draw_square(box, 140, -200, 110, "pink")
    draw_square(box, -14, -228, 30, "brown")
    draw_star(star, -160, -190, 50)
    draw_star(star, 170, -190, 50)
    #draw the star
    draw_star(star, -58, 310, 100)
    done()


def draw_triangle(turtle: Turtle, x: int, y: int, leg_length: int, base_length: int) -> None:
    """This function draws an isosceles triangle. User will input the location and length of legs and base."""
    turtle.hideturtle()
    turtle.color(56, 163, 62)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(leg_length)
    turtle.right(135)
    turtle.forward(base_length)
    turtle.right(135)
    turtle.forward(leg_length)
    turtle.end_fill()


def draw_circle(turtle: Turtle, x: int, y: int, rad: int) -> None:
    """This function draws a circle. User will input the location and desired radius."""
    turtle.hideturtle()
    turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


def draw_star(turtle: Turtle, x: int, y:int, side_length: int) -> None:
    """This is a recursive function that draws a star. The function draws the star smaller and smaller to create a cool pattern."""
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("gold")
    turtle.begin_fill()
    i: int = 0
    while (i < 100):
        turtle.forward(side_length)
        turtle.right(144)
        i += 1
        side_length *= .97
    turtle.end_fill()


def draw_square(turtle: Turtle, x: int, y:int, width: int, color: str) -> None:
    """This function draws a square. The user inputs the location, width and color they want the square to be."""
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    i: int = 0
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


main()


if __name__ == "__main__":
    main()