from math import sqrt

def mysqrt(a):
    x = a/2 
    while True: 
        y = (x+a/x) / 2
        if y == x:
            break
        x = y 
        return x

    print('a\tmsqrt(a)\t\tmath.sqrt(a)\t\tdiff')
print('------------------------------------------------------------------------------')
for a in range(1,9):
    my_root = mysqrt(a)
    py_root = sqrt(a)
    dif = py_root - my_root
    print('{:{align}{width}}'.format(a, align='<', width='8') + '{:{align}{width}}'.format(my_root, align='<', width='24')+'{:{align}{width}}'.format(py_root, align='<', width='24')+'{:{align}{width}}'.format(dif, align='<', width='10'))

