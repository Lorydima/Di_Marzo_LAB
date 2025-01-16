# Logo Tommy Hilfiger 

# Libreria Turtle
from turtle import *

# Turtle Setup
turtle = Turtle()

# Colore riempimento turtle
R = 2
G = 21
B = 78
turtle.fillcolor((R/255, G/255, B/255))
turtle.pencolor("black")

# Spessore Turtle
turtle.pensize(3)

# Velocità Tartaruga
turtle.speed(8)

# Funzione Creazione Logo 
def Funzione_Disegno_Logo_Tommy_Hilfiger():

    # Introduzione
    print("Disegno Logo Tommy Hilfiger")
    
    # Disegno Rettangolo Blu 1
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.end_fill()

    # Disegno Rettangolo Bianco 
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.goto(0,-40)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.end_fill()

    # Disegno Rettangolo Rosso 
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.goto(60,-40)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.end_fill()

   # Disegno Rettangolo Blu 
    turtle.fillcolor((R/255, G/255, B/255))
    turtle.begin_fill()
    turtle.goto(0,-80)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.end_fill()

    # Testo "Tommy Hilfiger"
    turtle.goto(-120,-80)
    turtle.write("Tommy",font=("Arial", 25, "normal"))
    turtle.goto(130,-80)
    turtle.write("Hilfiger",font=("Arial", 25, "normal"))

    # Nascondi Tartaruga
    turtle.hideturtle()
    
Funzione_Disegno_Logo_Tommy_Hilfiger()

wait = input("Premi Invio per chiudere il programma")