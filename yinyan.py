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

