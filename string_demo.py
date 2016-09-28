#team = 'New England Patriots'
#print(team[1])



prefixes = 'JHLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)

