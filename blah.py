from math import sqrt

i = float(input('Please input an integer to be factored '))

def my_factor(x):
    """
    my_factor takes an integer and returns a list containing the factors of the integer
    1. the function only needs to check the numbers up through the square root of the integer, because any factor
        larger than the square root will have the corresponding factor that is less than the square root 
        (i.e. 25 and 5 for 100)
    2.if the integer can be evenly divided by the number that's being checked, add that number
        as well as the integer divided by that number
    """
    factor_list = []
    x = int(x)
    for num in range(1, int(sqrt(x)+1)):
        if x % num == 0:
            factor_list.append(num)
            factor_list.append(int(x / num))
    return factor_list

print(my_factor(i))