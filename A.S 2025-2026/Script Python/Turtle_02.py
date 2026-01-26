# Lezione 19/01/2026 "Turtle_02"

# Library for program Dev
from turtle import *
import math

# Screen Setup
title("Isoscele triangle circle")
setup(1000,1000)
setworldcoordinates(-500,-500,500,500)

# Turtle Setup
hideturtle()
tracer(0,0)

# Main Function
'''
This is the main function that draw the isoceles triangles in a circle.
'''
def isoscele_triangle(x, y, width ,height, color, direction):
    up()
    goto(x,y)
    seth(direction-90)
    fd(width/2)

    # Bottom left corner
    p1x , ply = xcor(), ycor()
    back(width)

    # Botton right corner
    p2x, p2y = xcor(), ycor()

    goto(x,y)
    seth(direction)
    fd(height)

    # Top corner
    p3x, p3y = xcor(), ycor()

    goto(p1x,ply)
    down()
    fillcolor(color)
    begin_fill()
    goto(p2x,p2y)
    goto(p3x,p3y)
    goto(p1x,ply)
    end_fill()

# Parameters of circle
n = 12
r = 300
width = 2 * r * math.sin(math.radians(180/n))
height = 200

# Main Loop
def main_loop():
    '''
    Main loop that draw for n times the cirlce with the isosceles triangles
    '''
    for i in range(n):
        isoscele_triangle(r * math.cos(math.radians(180/n)) * math.cos(math.radians(i * 360/n))*
                         math.cos(math.radians(i*360/n)),
                          r*math.cos(math.radians(180/n))*
                          math.sin(math.radians(i*360/n)),
                          width, height, i*360/n, "blue")

done()
