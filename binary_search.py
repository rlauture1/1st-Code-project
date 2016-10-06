def binary_search(the_lsit, x):
    """"
    the function adopts bisection/binary search to find the index of a given number 
    in an ordered list

    the_list: an ordered list of numbers from least to greates

    x: number

    """"

    the_list.sort()
    beg = 0
    end = len(the_list)
    index = 0
    while end - beg > 0:
        if x == the list