age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age= int(input('how old are you?'))
if age >= 21:
    print('your age is {}'.format(age))
    print('your age is' + str(age)+ '.')
    print('yes, you can.')
elif age >= 6:
    print('your age is', age)
    print('you are a teenager. No, you cannot.')
else:
    print('your age is', age)
    print('no, not allowed.')

input()