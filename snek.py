#imports
import random
import turtle
import time
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

delay = 0.1

#Window Setup 
GameWindow = turtle.Screen()
GameWindow.title('Snake: Python Edition')
GameWindow.bgcolor('Black')
GameWindow.bgpic("GameAreaFinal.png")
GameWindow.setup(500, 500)
GameWindow.tracer(0)


width, height = 500, 500

minX, maxX = -width/2, width/2
minY, maxY = -height/2, height/2


#Food Spawning, Points 
Head = turtle.Turtle()
Head.speed(0)
Head.shape("square")
Head.color("white")
Head.penup()
Head.goto(0, 100)
Head.direction = "stop"
 
Food = turtle.Turtle()
Food.speed(0)
Food.shape("circle")
Food.color("orange")
Food.penup()
Food.shapesize(0.80, 0.80)
Food.goto(random.randint(50,100), random.randint(50,100))
 
Tails = []
Score = 0
 
Write = turtle.Turtle()
Write.speed(0)
Write.shape("square")
Write.color("white")
Write.penup()
Write.hideturtle()
Write.goto(0, 400)
Write.write("Score: {}".format(Score), align="center", font=("Arial", 24, "normal"))

#Movement 
def Move():
    if Head.direction == "up":
        y = Head.ycor()
        Head.sety(y + 20)
    if Head.direction == "down":
        y = Head.ycor()
        Head.sety(y - 20)
    if Head.direction == "right":
        x = Head.xcor()
        Head.setx(x + 20)
    if Head.direction == "left":
        x = Head.xcor()
        Head.setx(x - 20)
 
def go_up():
    if Head.direction != "down":
        Head.direction = "up"
def go_down():
    if Head.direction != "up":
        Head.direction = "down"
 
 
 
 
 
def go_right():
    if Head.direction != "left":
        Head.direction = "right"
def go_left():
    if Head.direction != "right":
        Head.direction = "left"
GameWindow.listen()
GameWindow.onkey(go_up, "Up")
GameWindow.onkey(go_down, "Down")
GameWindow.onkey(go_right, "Right")
GameWindow.onkey(go_left, "Left")
 
while True:
    GameWindow.update()
 
    if Head.xcor() > 300 or Head.xcor() < -300 or Head.ycor() > 300 or Head.ycor() < -300:
        time.sleep(1)
        Head.goto(0, 0)
        Head.direction = "stop"
 
        for Tail in Tails:
            Tail.goto(1000, 1000)
        Tails = []
 
        Score = 0
        delay = 0.1
 
        Write.clear()
        Write.write("Score: {}".format(Score), align="center", font=("Arial", 24, "normal"))
 
    if Head.distance(Food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        Food.goto(x, y)
 
        NewTail = turtle.Turtle()
        NewTail.speed(0)
        NewTail.shape("square")
        NewTail.color("white")
        NewTail.penup()
        Tails.append(NewTail)
 
        delay -= 0.001
 
        Score = Score + 10
        Write.clear()
        Write.write("Score: {}".format(Score), align="center", font=("Arial", 24, "normal"))
 
    for index in range(len(Tails) - 1, 0, -1):
        x = Tails[index - 1].xcor()
        y = Tails[index - 1].ycor()
        Tails[index].goto(x, y)
 
    if len(Tails) > 0:
        x = Head.xcor()
        y = Head.ycor()
        Tails[0].goto(x, y)
 
    Move()
 
    for segment in Tails:
        if segment.distance(Head) < 20:
            time.sleep(1)
            Head.goto(0, 0)
            Head.direction = "stop"
            for segment in Tails:
                segment.goto(1000, 1000)
            Tails = []
            Score = 0
            Write.clear()
            Write.write('Score: {}'.format(Score), align='center', font=('Arial', 24, 'normal'))
            hiz = 0.15
 
    time.sleep(delay)
