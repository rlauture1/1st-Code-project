def is_palindrome(my_string):
    """
    the palindrome function takes a string and returns True if the string is a palindrome and False if it is not
    1. the stop value on the recursion is if the string has a length of 1 or 0
    2. if the outer characters are the same, run the palindrome function on the middle of the string (excluding the outer characters)
    3. if the outer characters are not the same, the string isn't a palindrome
    """
    if len(my_string) <= 1:
        return True
    elif my_string[0] == my_string[len(my_string)-1]:
        return is_palindrome(my_string[1:len(my_string)-1])
    else:
        return False