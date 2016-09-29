#1
prefixes = 'JHLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)

#2
def character_count(first_string, a):
    answer = 0
    for letter in first_string:
        if letter ==a:
            answer+= 1
    return answer
 #3   
def word_value(word):
    total = 0 
    for letter in word: 
        total += ord(letter) - 96
    return total 

def receipt(groceries_list):
    grand_total = 0
    for word in groceries_list:
        print('{:{align}{width}}'.format(word, align='<', width='13')+'{:{align}{width}}'.format('$'+ str(word_value(word)), align='>', width='5'))
        grand_total += word_value(word)
    print('--------------------------')
    print('{:{align}{width}}'.format('Total', align='<', width='13')+'{:{align}{width}}'.format('$'+ str(grand_total), align='>', width='5'))
 
item_list = ['bananas', 'rice', 'paprika', 'potato chips']
 
receipt(item_list)


#4

#1 checks if the first letter is lowercase if it is it will return true if not, it will return false. 
#2 checks only the letter c if it is lowercase
#3 The output would be flag because is assigned.
#4 If any of the characters are found lowercase the output would be flag. 
#5 If no characters are lowercase the outout would be false. 

#5

def rotate_word(my_word, rotate):
    final_string = ''
    for char in my_word:
        if char.isalpha():
            new_letter = chr((ord)(char.lower()) - 97 + rotate) % 26 + 97
    else:
        final_string += char
    return final_string