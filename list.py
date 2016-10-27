def nested_sum(t):
    "Computes the total of all numbers in a list of lists"

    final = 0
    for obj in t:
        final += sum(object)
    return final

    
def cumsum(t):
    #Computes the cumlative sum of the numbers in
        #t. 
        
        #t: list of numbers
        
        #returns: list of numbers 
        #Expected output:
        #>>> t = [1,2, 3]
        #>>> cumsum(t)
        #[1, 3, 6]

        result = []
        total = 0
        for i in t: 
            total += i 
            results.append(total)
        return result 

def middle(t):
    #Returns all but the first and last elements of t.
    #t: list

    #returns: new list

    #Expected output:
    #>>> t = [1, 2, 3, 4]
    #>>> middle(t)
    #[2, 3] 
                      
       
    new_list = [t[1], t[2]]
    return new_list

def chop(t):
    #Removes the first and last elements of t.

    #t: list

    #return: None

    #Expected output:
    #>>> t = [1, 2, 3, 4]
    #>>> chop(t)
    #>>> [2, 3]
    
    t.pop()
    t.pop(0)

def is_sorted(t):
    #Checks whether a list is sorted. 
    
    #t: list

    #returns: boolean

    #Expected output:
    #>>>is_sorted([1, 2, 2])
    #True
    #>>> is_sorted(['b','a'])
    #False
    
    

    new_list = t[:]
    new_list.sort
    return new_list == t

def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to spell
    spell the other 

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output: 
    >>>is_anagram('stop', 'pots')
    True
    >>> is_anagram([1, 2, 2], [2,1, 2] 
    True
    """
    item1 = list(word1)
    item2 = list(word2)
    for obj in item1:
        if obj in item2:
            item2.remove(obj)
        else:
            return False
    return True

def has_duplicates():
   """Returns Trues if any element appears more than once in a sequence.

    #s: string or list

    returns: bool
    """
for i in s:
    if s.count(i)>1:
        return True 
    return False 

def has_adjacent_duplicates():
    """"Returns True if there are two adjacent elements. 

    s: string or list

    returns: bool 

    output:

    >>> print(has_adjacent_duplicates('cba'))"""

    new = list(s)
    for i in range(len(new)-1)
        if new[i] == new[i+1]:
            return True
    return False

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b','a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

    print(has_adjacent_duplicates('aba'))
    print(has_adjacent_duplicates('abba'))

    if_name_ == '_main_'
      main()
      
        

