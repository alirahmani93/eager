###########  Taklif 3  ############
###part 1: find_word_horizontal
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
