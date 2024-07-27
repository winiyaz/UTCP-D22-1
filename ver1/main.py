# Pong Game

from turtle import Screen, Turtle

# Screen setup
scr = Screen()
scr.bgcolor("#020617")
scr.setup(1000, 800)
scr.title("SitOnFace")

padle = Turtle()
padle.shape("square")
padle.color("#22c55e")
padle.shapesize(stretch_wid=5,stretch_len=1)



# -- Exit on Click
scr.exitonclick()