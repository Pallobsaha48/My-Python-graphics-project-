from turtle import*
import colorsys

speed(0)
bgcolor('black')
h=0.2
pensize (2)
for i in range(180):
c=colorsys.hsv_to_rgb (h,1,1)
ht=0.002
fillcolor (c)
begin_fill()
circle (180-1,70)
It (80)
circle (180-1,70)
rt (20)
for j in range (4):
rt (60)
It(120)
end_fill()
done()
