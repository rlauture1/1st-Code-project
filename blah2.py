import random
import turtle
import math
drunkard = turtle.Turtle()
#drunkard.shape('turtle')
#drunkward.turtlesize(.5,.5,.5)
print(drunkard)

def drunkWalk(n):
    """
    the drunkard function takes n, the number of moves the drunkard will take
    1. create variables for the north/south and east/west directions
    2. create variables for the direction of the drunkard at the end of his journey
    3. for n moves, a random number between 0 and 4 is generated - each corresponds to a cardinal direction
        a. the north/south or east/west value is changed depending on the generated number
        b. the direction is printed for the User
        c. set the turtle's heading to that direction and move it forward
        d. stamp the turtle's shape so the user can see where it is going'
    4. the final directions from the origin are translated
    """
    #draw a circle so that I can see the origin
    drunkard.circle(5)
    ns = 0
    ew = 0
    ns_direction = ''
    ew_direction = ''
    for block in range(n):
        direction = random.randrange(0,4)
        if direction == 0:
            ns += 1
            print('The drunkard walks North')
            drunkard.setheading(90)
        elif direction == 1:
            ew += 1
            print('The drunkard walks East')
            drunkard.setheading(0)
        elif direction == 2:
            ns -= 1
            print('The drunkward walks South')
            drunkard.setheading(270)
        else:
            ew -= 1
            print('The drunkard walks West')
            drunkard.setheading(180)
        drunkard.fd(30)
        drunkard.stamp()
    if ns >= 0:
        ns_direction = 'North'
    else:
        ns_direction = 'South'
    if ew >= 0:
        ew_direction = 'East'
    else: 
        ew_direction = "West"
    print('The drunkard has walked a total distance of %s blocks to the %s and %s blcoks to the %s' %(abs(ns), ns_direction, abs(ew), ew_direction))
    #have drunkard rotate so that I can see where the drunkard ended up
    while True:
        drunkard.lt(2)

drunkWalk(70)

turtle.mainloop()
