I import turtle
a=turtle.Turtle ()
a.color('cyan')
a. speed (0)
a.hideturtle ()
s=turtle.Screen() 
s.bgcolor('black')

for x in range (200):
    a. forward (x) 
    a.left(x-1) 
turtle.done()
