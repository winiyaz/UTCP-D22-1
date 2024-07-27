# This is the ball

from turtle import Turtle


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.color("#eab308")
		self.shape("circle")
		self.penup()

	def move(self):
		new_x = self.xcor() + 15
		new_y = self.ycor() + 10
		self.goto(new_x, new_y)
