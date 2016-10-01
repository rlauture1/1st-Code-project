fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)


def read_long_words():
    """
    prints only the words with more than 20 characters

    """
    pass

def has_no_e(word):
    """
    returns True if the given word doesn't have letter "e" in it. 
    """"
