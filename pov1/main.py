# Pong Game

import time
from turtle import Screen

from ball import Ball
from padl import Padl
from score import ScoreB

# Screen setup
scr = Screen()
scr.bgcolor("#020617")
scr.setup(1000, 800)
scr.title("SitOnFace")
scr.tracer(0)

r_padl = Padl((450, 0))
l_padl = Padl((-450, 0))
ball = Ball()
scob = ScoreB()

scr.listen()
scr.onkey(r_padl.go_up, "Up")
scr.onkey(r_padl.go_do, "Down")
scr.onkey(l_padl.go_up, "w")
scr.onkey(l_padl.go_do, "s")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	scr.update()
	ball.move()

	# Detect Collision with the wall
	if ball.ycor() > 380 or ball.ycor() < -380:
		ball.bounce_y()

	# Detect collission with right paddle
	if ball.distance(r_padl) < 50 and ball.xcor() > 340 or ball.distance(l_padl) < 50 and ball.xcor() < -340:
		ball.bounce_x()

	# Detect when right padle misses
	if ball.xcor() > 500:
		ball.reset_position()

	# Detect Left Sided miss
	if ball.xcor() < -500:
		ball.reset_position()

# -- Exit on Click
scr.exitonclick()
