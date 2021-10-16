# DICTIONARY METHOD

### Tamrin 1: sorted key
def _sorted_keys_sample_(sample_dictionary):
    # Use the built in keys() function
    # to generate a dictionary view
    keys = sample_dictionary.keys()
    # change dictionary view to list
    keys = list(keys)
    keys.sort()
    return keys
### Tamrin 2: sorted Values
def _sorted_values_sample_(sample_dictionary):
    # Use the built in keys() function
    # to generate a dictionary view
    values = sample_dictionary.values()
    # change dictionary view to list
    values = list(values)
    values.sort()
    return values
### Tamrin 3:
def _dictionary_names_grades_sample_(sample_dictionary):
    output_list = []
    keys = sample_dictionary.keys()
    for k in keys:
        each_list = sample_dictionary[k]
        grade1, grade2, grade3 = each_list[0], each_list[1], each_list[2]
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            output_list.append(k)
    return output_list
### Tamrin 4: Values have Key
def _return_keys_list_sample_(sample_dictionary, sample_value):
    keys_list = []
    for each_key in sample_dictionary.keys():
        if sample_value in sample_dictionary[each_key]:
             keys_list.append(each_key)
    keys_list.sort()
    return keys_list
### Tamrin 5: Count alphabet 
def _dictionary_of_letter_counts_sample_(sample_string):
    stripped_string = sample_string.replace(" ", "")        # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()     # convert to lower case
    sample_dictionary = {}
    # Iterate through the lowercase stripped string and set each
    # character as a key and its count as the value
    for character in lowercase_stripped_string:
        sample_dictionary[character] = lowercase_stripped_string.count(character)
    return sample_dictionary
### Tamrin 6: Count vovle alphabet
def _dictionary_of_vowel_counts_sample_(sample_string):
    stripped_string = sample_string.replace(" ", "")        # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()     # convert to lower case
    sample_dictionary = {}
    vowels = ["a", "e", "i", "o", "u"]
    # Iterate through the given string and set each 
    # character as a key and its count as the value
    for character in lowercase_stripped_string:
        if character in vowels:
            sample_dictionary[character] = lowercase_stripped_string.count(character)
    return sample_dictionary
### Tamrin 7: Count Word
def _dictionary_of_word_counts_sample_(sample_string):
    lowered_splitted_string = sample_string.lower().split()
    sample_dictionary = {}
    for word in lowered_splitted_string:
        sample_dictionary[word] = lowered_splitted_string.count(word)
    return sample_dictionary
### Tamrin 8: change number to Word
def _single_digit_words_sample(sample_integer):
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"1" : "one",
                         "2" : "two",
                         "3" : "three",
                         "4" : "four",
                         "5" : "five",
                         "6" : "six",
                         "7" : "seven",
                         "8" : "eight",
                         "9" : "nine",
                         "0" : "zero"}
    output_string = ""
    for integer in splitted:
        output_string += sample_dictionary[integer] + " "
    # remove any trailing whitespace
    stripped = output_string.rstrip(" ")
    return stripped

### Tamrin 9: Weekday

## Algoritm for this problrm:::::
# Assume that input was "May 5 1992"
#day (d) = 5        # It is the 5th day
#month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
#century (c) = 19   # the first two characters of the century
#year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# Formula and calculation
#day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
#after calculation we get, (w) = 2
#Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6

def _day_of_the_week_sample_(string):
    import math
    my_month, day, year = string.split(" ")
    months = {"March": 1,
              "April": 2,
              "May": 3,
              "June": 4,
              "July": 5,
              "August": 6,
              "September": 7,
              "October": 8,
              "November": 9,
              "December": 10,
              "January": 11,
              "February": 12}
    weeks = {"Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6}
    # Get the appropriate month as an int using a dictionary
    month = months[my_month]
    day = int(day)
    # The first two characters of the year
    century = int(year[0] + year[1])
    # The last two characters of the year
    year = int(year[2] + year[3])
    # If month > 10 (i.e january or february then substract one year)
    if month > 10:
        year = year - 1
    # Calculation
    w = (day + math.floor(2.6*month - 0.2) -2*century + year + math.floor(year/4) + math.floor(century/4))%7
    for day in weeks:
        if weeks[day] == w:
            return day

### Tamrin 10: Change number to single word
        
def _single_digit_words_sample(sample_integer):
    # Note that this is just one way
    # of solving this problem
    # It can be solved in many different ways
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"0" : ["zero", ""],
                         "1" : ["one", ""],
                         "2" : ["two","twenty"],
                         "3" : ["three","thirty"],
                         "4" : ["four","forty"],
                         "5" : ["five","fifty"],
                         "6" : ["six","sixty"],
                         "7" : ["seven","seventy"],
                         "8" : ["eight","eighty"],
                         "9" : ["nine","ninety"],
                         "10" : "ten",
                         "11" : "eleven",
                         "12" : "twelve",
                         "13" : "thirteen",
                         "14" : "fourteen",
                         "15" : "fifteen",
                         "16" : "sixteen",
                         "17" : "seventeen",
                         "18" : "eighteen",
                         "19" : "nineteen"}

    thousand_digit = sample_dictionary[splitted[0]][0]
    hundred_digit = sample_dictionary[splitted[1]][0]
    ten_digit = sample_dictionary[splitted[2]][0]
    one_digit = sample_dictionary[splitted[3]][0]

    my_list = []
    # Work with the thousand digit
    my_list.append(thousand_digit)
    my_list.append("thousand")

    if hundred_digit != "zero":
        my_list.append(hundred_digit)
        my_list.append("hundred")

    if ten_digit == "zero" and one_digit != "zero":
        my_list.append(one_digit)

    if ten_digit != "zero" and one_digit == "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)

    if ten_digit != "zero" and ten_digit != "one" and one_digit != "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)
        last_digit = sample_dictionary[splitted[3]][0]
        my_list.append(last_digit)

    if ten_digit != "zero" and ten_digit == "one" and one_digit != "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    if ten_digit != "zero" and ten_digit == "one" and one_digit == "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    # remove any "" that the list contains
    # due to the way the program was implemented
    if "" in my_list:
        my_list.remove("")
    out_string = ""
    out_string = ' '.join(my_list)
    return out_string

