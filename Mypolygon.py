#import turtle
#def squre(t):
 #   for i in range(4):
  #      t.fd(100)
   #     t.lt(90)

   
#def squre(t, length):
 #   t.fd(length)
  #  t.lt(90)
  #  t.fd(length)
  #  t.lt(90)
   # t.fd(length)
    #t.lt(90)
    #t.fd(length)
    #print(t)
   
    #def polygon(t, length, n):
    #t.fd(length)
    #t.lt(90)
    #t.fd(length)
    #t.lt(90)
    #t.fd(length)
    #t.lt(90)
    #t.fd(length)
    #print(t)

#jerry = turtle.Turtle()

#squre(jerry)

#teresa = turtle.Turtle()
#squre(teresa, 300)



#turtle.mainloop()



import turtle


def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

import math

def circle(t, r):
    circumference = 2* math.pi * r
    n = 50
    length = circumference / n 
    polygon(t, n, length)

jerry = turtle.Turtle()
circle(jerry, 80)
