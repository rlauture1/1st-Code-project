import turtle
import math
flowercircle = turtle.Turtle()
flowercircle.pensize(4)

print(flowercircle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t,n, length):
    angle = 360.0/ n 
    polyline(t, n, length, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n 
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/ 360
    n = int(arc_length / 3) + 1 
    step_length = arc_length / n
    step_angle = float(angle) / n 
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(0,2):
        arc(t, r, angle)
        t.lt(180-angle)

for i in range(0,6):
    petal(flowercircle, 200, 360/6)
    flowercircle.lt(360/6)
arc(flowercircle, 200, 360/6)
flowercircle.lt(61)
circle(flowercircle,200)

turtle.mainloop()



import turtle
import math
triangle = turtle.Turtle()
triangle.pensize (4)

print(triangle) 

def twotris(t):
   t.lt(30)
   t.fd(200)
   t.rt(120)
   t.fd(200)
   t.rt(120)
   t.fd(400)
   t.lt(120)
   t.fd(200)
   t.lt(120)
   t.fd(200)
   
twotris(triangle) 

triangle.lt(60)
twotris(triangle)

triangle.fd(200)
triangle.lt(91)
triangle.circle(200)
triangle.lt(90)
triangle.fd(100)
triangle.circle(55)

triangle.fd(100)
triangle.lt(30)

triangle.fd(100)
triangle.circle(55)

triangle.lt(180)
triangle.fd(100)

triangle.rt(270)
triangle.fd(100)
triangle.circle(55)

triangle.lt(180)
triangle.fd(100)

triangle.rt(270)
triangle.fd(100)
triangle.circle(55)






turtle.mainloop()



turtle.mainloop()



import turtle
import math
yinyan = turtle.Turtle()
yinyan.pensize(4)

print(yinyan)

def yin(radius, color1, color2):
    yinyan.width(3)
    yinyan.color("black", color1)
    yinyan.begin_fill()
    yinyan.circle(radius/2., 180)
    yinyan.circle(radius, 180)
    yinyan.left(180)
    yinyan.circle(-radius/2., 180)
    yinyan.end_fill()
    yinyan.left(90)
    yinyan.up()
    yinyan.forward(radius*0.35)
    yinyan.right(90)
    yinyan.down()
    yinyan.color(color1, color2)
    yinyan.begin_fill()
    yinyan.circle(radius*0.15)
    yinyan.end_fill()
    yinyan.left(90)
    yinyan.up()
    yinyan.backward(radius*0.35)
    yinyan.down()
    yinyan.left(90)

def main():
    reset()
    yin(yinyan, 200, "black", "white")
    yin(yinyan, 200, "white", "black")
    ht()
  
    return "Done!"

    if _yinyan_ == '_main_':
        yinyan.main()
        yinyan.mainloop()