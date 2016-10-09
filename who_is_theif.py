"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.
Among them, three were telling the truth while one was lying.
Could you find out who is the thief?
"""

for theif in ['John','Paul','George','Ringo']:
    sum = (theif != 'John') + (theif == 'George') + \
        (theif == 'Ringo') + (theif != 'Ringo')
    if sum == 3:
        print('The theif is {}.'.format(theif))