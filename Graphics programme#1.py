import turtle as t
t.bgcolor('white')
t.speed(50)
t.pensize(5)
t.goto(-300,100)
for i in range(10):
	c = ['red','black']
	t.color(c[i%2])
	t.begin_fill()
	for j in range(4):
		t.rt(109)
		t.circle(140,-100)
	t.rt(10)
	t.lt(90)
	t.end_fill()
t.done()
