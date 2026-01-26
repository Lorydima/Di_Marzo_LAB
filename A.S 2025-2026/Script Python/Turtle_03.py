# Lezione 26/01/2026 "Turtle_03"

# Library for program Dev
import turtle
import math

# Screen Setup
screen = turtle.Screen()
screen.title("Beating Heart")
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)

# Turtle Setup
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)
turtle.color("red")

# Heart Function
def heart(alpha,d):
    radius = d/math.tan(math.radians(180-alpha/2))
    turtle.up()
    turtle.goto(0,-d*math.cos(math.radians(45)))
    turtle.seth(90 - (alpha-180))
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(d)
    turtle.circle(radius, alpha)
    turtle.left(180)
    turtle.circle(radius,alpha)
    turtle.forward(d)
    turtle.end_fill()
