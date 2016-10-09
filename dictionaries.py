#names = ['Rose', 'Jerry', 'Alex']
#scores = [95, 75, 85]
#print(scores[names.index()])

grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

grades['Brian'] = 90
print(grades)

print(len(grades))
print('Jerrry' in grades)
print(90 in grades.values())

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('Bookeeper')
print(h)




