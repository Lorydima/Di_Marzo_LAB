# Lezione 23/02/2026 "Turtle_04"

# Library for program Dev
import turtle
import math

# Screen Setup
screen = turtle.Screen()
screen.title("Circles")
screen.setup(1000,1000)

# Turtle Setup
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)

# Circles Function
def draw_circles(x,y,radius):
    '''
    This function set the circles
    '''
    turtle.up()
    turtle.goto(x,y-radius)
    turtle.seth(0)
    turtle.down()
    turtle.circle(radius,steps=360)

# Variabiles
'''
Circles Coordinates
'''
r = 150
n = 5
r2 = r/2/math.sin(math.radians(180/n))
angle = 90

# Main Function
'''
Main Functions thath draws the circles
'''
def main(angle):
    for i in range(n):
        draw_circles(r2*math.cos(math.radians(angle)), r2*math.sin(math.radians(angle)), r)
        angle += 360/n 

# Call Main Function
main(angle)
turtle.done()
