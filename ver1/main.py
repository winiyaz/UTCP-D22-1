# Pong Game

from turtle import Screen, Turtle

# Screen setup
scr = Screen()
scr.bgcolor("#020617")
scr.setup(1000, 800)
scr.title("SitOnFace")

# Setting up the padle
padle = Turtle()
padle.shape("square")
padle.color("#22c55e")
padle.shapesize(stretch_wid=5, stretch_len=1)
padle.penup()
padle.goto(450, 0)


def go_up():
	new_y = padle.ycor() + 20
	padle.goto(padle.xcor(), new_y)


def go_do():
	new_y = padle.ycor() - 20
	padle.goto(padle.xcor(), new_y)


scr.listen()
scr.onkey(go_up, "Up")
scr.onkey(go_do, "Down")

# -- Exit on Click
scr.exitonclick()
