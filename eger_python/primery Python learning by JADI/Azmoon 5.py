my_list = [[3,4],[6,7],[10,12]]
print(my_list[0:2])

my_list = [[3,5,6], [6,4,2], [9,4,8]]
for k in range (len(my_list)):
    my_list[k][0] = 1
print(my_list)

my_list = [[6,2],[3,9,5]]
x = 0
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x = x + my_list[m][k] 
print(x)

my_list = []
for m in range(0,2):
    new_list = []
    for k in range(4,6):
        new_list.append(k)
    my_list.append(new_list)
print(my_list)


my_list = [[3,5],[2,9],[4,7]]
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        my_list[m][k] = my_list[m][k] * 2
print(my_list)

numbers={1: "uno", 3:"two", "tres":3}
print(numbers.pop(3))

numbers={"one": [1,"uno"], "two": [2,"dos"]}
print (numbers["two"][1][2])


#d={1:"one", "two": 2 , 3: "tres"}
#print (d[2])

d={1:"one", "two": 2 , 3: "tres"}
print (d.get(2))

#numbers = {["one","two"]: 1, "two": 2}
#print(numbers)

### part 2

def row_maximums(some_multi_dimensional_list):
    dictionary = {}
    count = 0

    for row in some_multi_dimensional_list:
        max_value = 0
        for col in row:
            if col > max_value:
                max_value = col
        dictionary ["row "+str(count)+" max"] = max_value
        count += 1
    return dictionary
### part 3:

#Write a function named construct_dictionary_from_lists that accepts 3 one dimensional lists and 
#constructs and returns a dictionary as specified below. 
#		The first one dimensional list will have n strings which will be the names of some people.
#		The second one dimensional list will have n integers which will be the ages that correspond to those people.
#		The third one dimensional list will have n integers which will be the scores that correspond to those people.
#Note that if a person has a score of 60 or higher (score >= 60) that means the person passed, if not the person failed.
#Your function should return a dictionary where each key is the name of a person and the value corresponding 
#to that key should be a list containing age, score, 'pass' or 'fail' in the same order as shown in the sample output.

names = ["paul", "saul", "steve", "chimpy"]
ages = [28, 59, 22, 5]
scores = [59, 85, 55, 60]

def construct_dictionary_from_lists(names, ages, scores):
    dictionary = {}
    grades = []

    #make a new list called grades where we evaluate if pass or fail
    for score in scores:
        if score >= 60:
            grades.append("pass")
        else:
            grades.append("fail")
                    
    #correct keys and values en dictionary
    for x in range(len(names)):
        dictionary[names[x]]= [ages[x], scores[x], grades[x]]

    return dictionary



#solution {'steve': [22, 55, 'fail'], 'saul': [59, 85, 'pass'], 'paul': [28, 59, 'fail'], 'chimpy': [5, 60, 'pass']}

### part 4:
def one_to_2D(some_list, r, c):
    mult_rc = r*c
    some_list_aux = []
    list_aux = []
    final_list = []

    #------------------------------------
    #first we compare is the leng of the list is greather or equal than the multiplication
    #of r*c if yes we split the list to fix it.
    if len(some_list) >= mult_rc:
        some_list_aux = some_list[:mult_rc]
    #if the len of the list is less thant the multiplication r*c then we fill the spaces
    #with None string
    else:
        some_list_aux = some_list
        for x in range(len(some_list_aux), mult_rc):
            some_list_aux.append(None)
    #print(some_list_aux)
    #-------------------------------------

    for x in some_list_aux:
        list_aux.append(x)
        if len(list_aux) == c:
            final_list.append(list_aux)
            list_aux = []

    return final_list

### part 5:
def multiplication_table(n):
    final_list = []
    for x in range(1,n+1):
        list_aux = []
        for z in range(1, n+1):
            list_aux.append(x*z)
            if len(list_aux) == n:
                final_list.append(list_aux)
    return final_list


##############################

def perform_multiplication(integer_1, integer_2):
    integer_2 = integer_1 * integer_2
    return integer_1, integer_2

# Main Program #
integer_1, integer_2 = perform_multiplication(8, 11)
print(integer_1, integer_2)
