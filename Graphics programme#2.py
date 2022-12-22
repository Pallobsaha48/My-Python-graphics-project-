from turtle import *

colors = ['red','purple','blue','green','yellow','orange']

bgcolor ('black')

for x in range (360):
	pencolor(colors[x%6])
	width (x/100+1)
	forward(x)
	left(59)
	speed(10)
	# you can reduce the speed as much as you want
