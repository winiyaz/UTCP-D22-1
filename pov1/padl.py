# Paddle class

from turtle import Turtle


class Padl(Turtle):

	def __init__(self, pos):
		super().__init__()
		self.shape("square")
		self.color("#22c55e")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(pos)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_do(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)
