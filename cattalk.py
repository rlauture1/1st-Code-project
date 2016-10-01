fin = open('words.txt')
def is_triple_double(word):
    """
    Tests if a word contains three consecutive double letters.
    word: string
    returns: bool
    """
    for line in fin:
        word = line.strip()
    l = 0 
    count = 0
    while l < len(word)-1:
        if word[l] == [l+1]:
            count = count +1
            if count == 3: 
                return True
            l = l+2
        else:
            count = 0
            l = l + 1 
        return False


def find_triple_double():
    """
    Reads a word list and prints words with triple double letters.
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
