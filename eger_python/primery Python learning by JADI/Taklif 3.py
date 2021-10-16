############### Taklif 3 ###################

### Part 3:
#Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters (like a crossword puzzle) 
#and a string (word) as input arguments. This function searches the rows and columns of the 2d list to find a match for the word. 
#If a match is found, this functions capitalizes the matched characters in 2-dimensional list and returns the list. 
#If no match is found, this function simply returns the origianl 2-dimensional list with no modification.

crosswords=[['s','d','o','g'],
			['c','u','c','m'],
			['a','x','a','t'],
			['t','e','t','k']]
word='cat'

#crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
#word='cat'

def find_word_horizontal(crosswords,word):
    matches = []

    for item_list in crosswords:
        if word in "".join(item_list):
            matches.append(item_list)

    if matches:
        final_list = [crosswords.index(matches[0]), matches[0].index(word[0])]
    else:
        return None
    return final_list

def find_word_vertical(crosswords,word):
    column_list = []
    column_number = []
    matches = []
    count = 0

    for x in range(len(crosswords)):
        aux_list = []
        for y in range(len(crosswords[x])):
            aux_list.append(crosswords[y][x])
        column_list.append(aux_list)

    for item_list in column_list:
        if word in "".join(item_list):
            matches.append(item_list)
            column_number.append(count)
        count += 1

    if matches:
        final_list = [matches[0].index(word[0]), column_number[0]]
    else:
        return None

    return final_list

def capitalize_word_in_crossword(crosswords,word):

    capitalize_vertical = find_word_vertical(crosswords,word)
    capitalize_horizontal = find_word_horizontal(crosswords, word)

    if capitalize_horizontal:
        row = capitalize_horizontal[0]
        column = capitalize_horizontal[1]

        for x in range(len(word)):
            crosswords[row][column] = crosswords[row][column].upper()
            column += 1

    #return crosswords

    elif capitalize_vertical:
        row = capitalize_vertical[0]
        column = capitalize_vertical[1]

        for x in range(len(word)):
            crosswords[row][column] = crosswords[row][column].upper()
            row += 1

    return crosswords

