# Lezione 02/03/2026,30/03/2026 and 13/04/2026 "Typing Game" Lorenzo Di Marzo 3E

# Library for program Dev
import turtle
import random

# Screen Setup
screen = turtle.Screen()
screen.title("Typing Game")
screen.setup(1000,1000)
screen.bgcolor("blue")
screen.tracer(0,0)

# Turtle Setup
turtle.hideturtle()
turtle.up()
turtle.color("red")

# Score Turtle Setup
score_turtle = turtle.Turtle()
score_turtle.color("red")
score_turtle.hideturtle()
score_turtle.up()
turtle.goto(350,400)
turtle.write("Score:" , align='center', font=('Courier', 25, 'normal'))

# Speed Variabiles
min_speed = 5
max_speed = 30

# General Array
speed = []
pos = []

# Letters Array
letters = []
lts = [] # letter on the screen
n_letters = 10

# Game Start Var
gameover = False
score = 0

# Difficulty Function
def difficulty():
    global min_speed, max_speed
    min_speed += 1
    max_speed += 1
    screen.ontimer(difficulty, 5000)

# Game Over function
def gameover():
    turtle.goto(0,0)
    turtle.color("red")
    turtle.write("GAME OVER" ,align='center', font=('Courier', 50, 'normal'))
    turtle.goto(0,-150)
    turtle.color("orange")
    turtle.write('Your Score is {}', format(score), align='center', font=('courier', 40, 'normal'))
    screen.update()

# Draw Score Function
def draw_score():
    score_turtle.clear()
    score_turtle.goto(420,400)
    score_turtle.write('{}', format(score), allign='center', font=('courier', 25, 'normal'))
    screen.update()

# Draw Letters Functions
def draw_letters():
    global gameover
    for i in range(len(letters)):
        lts[i].clear
        lts[i].goto(pos[i])
        lts[i].write(letters[i], allign='center', font=('courier', 20, 'normal'))   
        pos[i][1]-=[speed]
        if pos[i][1]<500:
            gameover = True
            return
    screen.update()
    screen.ontimer(draw_letters, 50)

# C Function
def C_function(c):
    global score
    if c in letters:
        score += 1
        pressed = letters.index(c)
        while True:
            L = chr(ord('a') + random.randrange(26))
            if L not in letters:
                letters[pressed] = L
                break
        pos[pressed] = [random.randint(-450,450), 500]
        speed[pressed] = random.radint(min_speed, max_speed)
    else:
        score -= 1
    draw_score()

