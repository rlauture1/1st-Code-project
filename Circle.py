from Point1 import *

class Circle:
    """A class of circles"""

Rose_circle = Circle()
Rose_circle.center = Point()
Rose_circle.center.x = 150
Rose_circle.center.y = 100
Rose_circle.radius = 75

def point_in_circle(c, p):
    """
    takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
    """
    d = distance_between_points(c.center, p)
    if d<=c.radius:
        return True
    else:
        return False

Rose_point = Point()
Rose_point.x = 150
Rose_point.y = 50
print(point_in_circle(Rose_circle, Rose_point))

Another_point = Point()
Another_point.x = 150
Another_point.y = 0
print(point_in_circle(Rose_circle, Another_point))

class Rectangle: 

Rose_rectangle = Rectangle()
Rose_rectangle.width = 20
Rose_rectangle.height = 35
Rose_rectangle_.corner = Point()
Rose_rectangle.x = 1
Rose_rectangle.y = 1 