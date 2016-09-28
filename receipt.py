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