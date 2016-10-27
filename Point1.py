class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

   
    def _str_(self):
        return 'This point is (%g, %g)'.format('+self.x +',' + self.y +')


# new_point = Point()
# new_point.x = 100
# new_point.y = 50
# print(new_point)

# my_point = Point()
# print(my_point)
# my_point.x = 3
# my_point.y = 4
# print(my_point.x)

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

# print_point(my_point)
# Alex_point = Point()
# Alex_point.x = 100
# Alex_point.y = 200
# print_point(Alex_point)


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    import math
    return math.sqrt((p2.x-p1.x)**2 + (p2.y - p1.y)**2)

# my_point = Point()
# my_point.x = 1 
# my_point.y = 1
# print_point(my_point)
# Alex_point = Point()
# Alex_point.x = 3
# Alex_point.y = 3 



class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """

# Jerry_rect = Rectangle()
# Jerry_rect.width = 10
# Jerry_rect.height = 20
# Jerry_rect.corner = Point()
# Jerry_rect.corner.x = 1
# Jerry_rect.corner.y = 1 

# print(Jerry_rect.corner.x)
# print_point(my_point)

# print(Jerry_rect.corner == my_point)
# print(Jerry_rect.corner is my_point)


def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# print_point(find_center(Jerry_rect))


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

# print(Jerry_rect.width, Jerry_rect.height)
# grow_rectangle(Jerry_rect, -4, -10)
# print(Jerry_rect.width, Jerry_rect.height)

def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner is', rect.corner.x, rect.corner.y)

# print_rectangle(Jerry_rect)
# grow_rectangle(Jerry_rect, -4, -10)
# print_rectangle(Jerry_rect)

def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point as instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',
            isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does box have an attribute x?', hasattr(box, 'x'))

    print('Does box have an attribute corner?', hasattr(box, 'corner'))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main()