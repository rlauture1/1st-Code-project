list_1 = [10,20]

AFC_east = ['New England Patriots', 'Buffalo Bills','Miami Dolphins','New York Jets' ]

a_nested_list= ['spam', 2.0, 5, [10, 20]]
print(AFC_east)

AFC_east[3] = 'New York Giants'
print(AFC_east[0:2])
print(AFC_east[2:4])
print(AFC_east[-2:])

L= [
    ['Apple', 'Googgle','Microsoft'],
    ['Java','Python',['Ruby','On Rail'],'PHP'],
    ['Adam','Bart','Lisa']
]

print(L[0][0])
print(L[2][2])
print(L[1][2][1])

for team in AFC_east:
    print(team)

numbers = [2,0,1,6,9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

my_list = ['spam', 1, ['New England Patriots','Buffalo Bills',
                        'Miami Dolphins','New York Giants']

          [[1,2,3]]
print(len,(my_list))

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

m = []
m.append(a)
m.append(b)
print(m)

print([0] * 4)
print(['Tom Brady', 'Bill Belichick'] * 3)
