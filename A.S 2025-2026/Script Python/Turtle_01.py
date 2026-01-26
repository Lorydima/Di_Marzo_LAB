# Lezione 12/01/2025 Turtle_01

# Library for program Dev
import turtle
import random

# Screen Setup
screen = turtle.Screen()
screen.setup(800,800)
screen.bgcolor("white")

# Turtle Setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0) 
turtle.tracer(0)

# Main Code
def main(x,y,side,angle,rotation,color):
    '''
    This code have all command that allow the turtle to draw.
    '''
    t.penup()
    t.goto(x,y)
    t.setheading(rotation)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for i in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180-angle)
    
    t.end_fill()
    t.penup()

# Main Loop
for j in range(50):
    '''
    This code defines all variabiles for the turtle and call the main
    '''
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    side = random.uniform(40, 120)
    angle = random.uniform(30, 150)
    rotation = random.uniform(0, 360)
    color = (random.random(), random.random(), random.random())
    main(x,y,side,angle,rotation,color)

# Final Commands
turtle.tracer(1)
turtle.done()
