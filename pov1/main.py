# Pong Game

from turtle import Screen, Turtle
from padl import Padl

# Screen setup
scr = Screen()
scr.bgcolor("#020617")
scr.setup(1000, 800)
scr.title("SitOnFace")
scr.tracer(0)

r_padl = Padl((450, 0))
l_padl = Padl((-450, 0))

scr.listen()
scr.onkey(r_padl.go_up, "Up")
scr.onkey(r_padl.go_do, "Down")
scr.onkey(l_padl.go_up, "w")
scr.onkey(l_padl.go_do, "s")

game_is_on = True
while game_is_on:
	scr.update()

# -- Exit on Click
scr.exitonclick()
