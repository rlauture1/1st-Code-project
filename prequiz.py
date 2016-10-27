def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    final = 0
    for obj in t:
        final += sum(obj)
    return final


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    new_list = []
    runningsum = 0
    for x in range(len(t)):
        runningsum += t[x]
        new_list.append(runningsum)
    return new_list


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    new_list = t[:]
    new_list.pop()
    new_list.pop(0)
    return new_list


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.pop()
    t.pop(0)


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    new_list = t[:]
    new_list.sort()
    return new_list == t


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    True
    """
    available1 = list(word1)
    available2 = list(word2)
    for obj in available1:
        if obj in available2:
            available2.remove(obj)
        else:
            return False
    return True


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    new = list(s)
    for obj in new:
        if new.count(obj) > 1:
            return True
    return False

def has_adjacent_duplicates(s):
    """
    returns True if the string contains any adjacent duplicates
    """
    new = list(s)
    for i in range(len(new)-1):
        if new[i] == new[i+1]:
            return True
    return False

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

    print(has_adjacent_duplicates('aba'))
    print(has_adjacent_duplicates('abba'))


if __name__ == '__main__':
    main()