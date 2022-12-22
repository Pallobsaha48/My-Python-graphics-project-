from turtle import*
import colorsys

speed(50)
bgcolor('black')
hue = 0.0
pensize(4)

for i in range(200):
	col = colorsys.hsv_to_rgb(hue, 1, 1)
	pencolor(col)
	hue += 0.005
	for j in range(2):
		lt(40)
		circle(i)
done()
