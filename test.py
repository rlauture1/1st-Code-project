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