
# Palindrom

def Palindrom(s):
    if str(s).lower() == str(s)[::-1].lower():
        return True
    else:
        return False
s= input("S: ")
cc= Palindrom(s)


# vowels alphabet

def voice(s):
    q=0
    v=["a",'e','i','o','u']
    s=s.lower()
    for char in (s):
        if char in v:
            q+=1
    return q
     
# First alphabet
s,c=input("sentence is: "),input("character is: ")
def repeat_cahr(s,c):
    q=0
    s=s.lower()
    s=s.title()
    c=c.capitalize()
    for char in s:
        if char in c:
            q+=1
            print(c, char, q)
    return q


def _count_words_given_character_sample_(s, c):
    
    splitted_string = s.lower().split()
    c=c.lower()
    
    my_count = 0
    for string in splitted_string:
        if string[0] == c:
            my_count = my_count + 1
            print(string, string[0], my_count)
    return my_count

# count character in Word
n= int(input("n: "))
def ccw(s,n):
    q=0
    words=s.split()
    print(words)
    for word in words:
        if len(word) >= int(n):
            q+=1
        #for i in range(1,len(word)+1):
            #print("word is: {}, i is: {}".format(word , i))
            #if int(i)>n:
                #q+=1
    return q
# Most frequency of characters in string

def mcs(s):     # most common character      in use: @replace @lower @count
    stripped_string = s.replace(" ", "")    # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()    # convert to lower case
    sample_character = None
    sample_maximum_count = 0

    # Iterate through the given string and for each character
    # set a count, among these counts,  return the character whose count is maximum
    # On case of tie, return the last character that occurs that has the most count
    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)
        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character
     


def reverse_string_sample(s):
    s=str(s)
    swaped_string = s.swapcase()
    reverse_string = ""
    return swaped_string
    """
    for char in str(swaped_string()):
        r= char + reverse_string
    return reverse_string
    """

    ### باقی نگه داشتن و معکوس کردن

def _preserve_and_reverse_sample_(string):
    splitted_list = string.split()
    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]
    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string



