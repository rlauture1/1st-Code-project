<<<<<<< HEAD
import math
=======
# This is not a function
'''
You need to begin with
def quadratic_equation(a, b, c):
    ...
'''

import cmath
>>>>>>> 9f53440f8e47383679dd3517e90b640a4679b3d3

def quadratic(a,b,c):
    A = b**2-4*a*c 
    if A >=0:
        X1 = ((-b + math.sqrt(A))/2*a)
        X2 = ((-b - math.sqrt(A))/2*a)
        return X1,X2

    else:
            print('No Real Number Soultion')

print(quadratic(2,2,2))
print(quadratic(1,5,6))