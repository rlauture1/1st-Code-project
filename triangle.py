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
