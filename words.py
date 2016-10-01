# fin = open('words.txt')
# line = repr(fin.readline())
# # https://docs.python.org/3/library/functions.html#repr

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)


def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
     if len(word) > 20: 
        print(word)


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    for letter in word:
        if letter == 'e':
            return False
        return True

print(has_no_e('Babson'))
print(has_no_e('College'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter in forbidden:
            return False
        return True
print(avoids('Babson, 'ab'))
print(avoids('College', 'ab'))
def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
        return True 

print(usesonly('Babson, 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True 


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word: 
        if letter < before: 
            return False 
return True

print(is_abecedarian('abs'))
print(is_abecedarian('college'))

exercise 3 finish for hw