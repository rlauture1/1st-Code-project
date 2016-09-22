def tower(height, source, bridge, destination):
    if height >= 1: 
       tower(height - 1, source, destination, bridge)
       print('%s --> %s' %(source, destination))
       tower(height - 1, bridge, source, destination)

tower(4,'A','B','C')

