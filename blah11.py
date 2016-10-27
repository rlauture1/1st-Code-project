import random

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

my_list = list(line.strip() for line in open('words.txt'))

def win_state(guessed_letters, secret_word):
    '''
    returns true if every letter in the secret word has been guessed
    '''
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def hangman(secret_word):
    '''
    Plays the game of hangman with the user
    User gets 8 incorrect guesses
    Returns True if the user wins, False if they lose
    '''
    print('Welcome to the game, hangman!')
    print('I am thinking of a word that is %d letters long' %(len(secret_word)))
    guesses = 8
    available = []
    #fills the 'available' list with every lowercase letter
    for i in range(97, 123):
        available.append(chr(i))
    guessed_letters = []
    #creates a loop for each turn that only breaks if the user has won or lost
    while guesses > 0 and win_state(guessed_letters, secret_word) == False:
        print('Available letters: ')
        print(available)
        revealed = ''
        player_guess = ''
        #forces the user to input a letter that hasn't been guessed yet
        while player_guess not in available:
            player_guess = str(input('Please guess a letter: '))
            player_guess = player_guess.lower()
        #adds the guess to the list of guessed letters
        guessed_letters.append(player_guess)
        #takes the guess from the list of available letters
        available.remove(player_guess)
        #creates a string where each letter is only revealed if it has been guessed
        for letter in secret_word:
            if letter in guessed_letters:
                revealed += letter
            else:
                revealed += '_'
        if player_guess in secret_word:
            print('Good guess: %s' %(revealed))
        else:
            guesses -= 1
            print('Oops! That letter is not in my word: %s' %(revealed))
        print('You have %d guesses left' %(guesses))
    if guesses == 0:
        print('You lose! The word is %s' %(secret_word))
        return False
    else:
        print('You win! The word is %s' %(secret_word))
        return True

hangman(chooseWord(my_list))