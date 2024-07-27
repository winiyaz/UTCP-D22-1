# Scoreboard file

from turtle import Turtle


class ScoreB(Turtle):

	def __init__(self):
		super().__init__()

		self.color("#22d3ee")
		self.penup()
		self.hideturtle()
		self.l_sco = 0
		self.r_sco = 0
		self.up_sc()

	def up_sc(self):
		self.clear()
		self.goto(-200, 250)
		self.write(self.l_sco, align="center", font=("Courier", 80, "normal"))
		self.goto(200, 250)
		self.write(self.r_sco, align="center", font=("Courier", 80, "normal"))

	def l_point(self):
		self.l_sco += 1
		self.up_sc()

	def r_point(self):
		self.r_sco += 1
		self.up_sc()
