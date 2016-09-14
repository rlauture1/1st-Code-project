import cmath

a= float(input('Enter a: '))
b= float(input('Enter b: '))
c= float(input('Enter c: '))

d=(b**2)- (4*a*c)

solution1 = (-b-cmath.sqrt(d))/(2*a)
solution2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(solution1,solution2))
