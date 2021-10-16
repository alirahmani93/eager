########  FINAL EXAM ########
### part 1:
def part_one_and_two():
    my_list = [[2,3],[6,5],[10,9]]
    print(my_list[0:2])

    my_list = []
    for m in range(0,2):
        new_list = []
        for k in range(2,4):
            new_list.append(k)
        my_list.append(new_list)
    print(my_list)
    my_list = []
    for k in range(1,101,10):
        my_list.append(k)
    print (my_list[: :3] )

    my_list = [2, 3, 4]
    for k in range (3):
        my_list.insert(-k, k+1)
    print(my_list)
    def my_fun(x):
        for k in range (len(x)):
            x.extend(x[:k])
    m = [2,4,3]
    my_fun(m)
    print(m)
    def my_fun(a):
        a[0] = 'new name'     
        a[1] = 'john'      

    x = ['old name', 'jack']
    my_fun(x)
    print (x)

    my_list = [[3,2],[2,6,4]]
    x = 0
    new_list=[]
    for m in range(len(my_list)):
        for k in range(len(my_list[m])):
            x =  my_list[m][k]
            new_list.append(x)        
    print(new_list)

    m = 0
    my_str_1 = "car"
    my_str_2 = "cat"
    for char_1 in my_str_1:
        for char_2 in my_str_2:
            if char_1 != char_2:
                m = m + 1
    print([m])

    x = "bye bob"
    print ([x.strip("b")])

    m = 0
    for x in range (4,6):
       for y in range (2,4):
          m = m + x + y
    print ([m])

    ### part 2:
    x = "mississipi"
    print (x.replace('i','z',2))

    x = ["duck", "car", "pet"]
    print ("AA".join(x))

    k = 10
    while k>2:
        x = k / 3
        k = k - 1
    print(x)

    numbers={"one": [1,"uno"], "two": [2,"dos"]}
    print (numbers["one"][1][2])

    #d={1:"one", "two": 2 , 3: "tres"}
    #print (d["tres"])

    my_string = "x = {0:#^7d} and y = {1:@>8.3f}".format(5, 0.3)
    print (my_string)

    print('A{0:B^9}C'.format('dog'))

    def my_fun(x):
        z = 0
        for item in x:
            m = x.count(item)
            if m >z:
                z = m
        return z

    y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
    print (my_fun(y))

    list_1 = ["cat", 3, "cat" , 25, 12]
    list_2 = ["car", 25, "dog" , 43]
    count = 0
    for item in list_1:
        if item in list_2:
            count = count + 1
    print (count)

    print('{0:,}'.format(12345678))

### Part 3: n letter dictionary
def n_letter_dictionary(argument):
	argument = argument.lower()
	list_argument = argument.split()
	dictionary = {}

	no_repeat_list = [] #palabras sin repetirse
	len_element_list = [] #len de las palabras sin repetirse
	for element in list_argument:
		if element not in no_repeat_list:
			no_repeat_list.append(element)
			len_element_list.append(len(element))

	no_repeat_number_list = []
	for number in len_element_list:
		if number not in no_repeat_number_list:
			no_repeat_number_list.append(number)
	no_repeat_number_list.sort()

	for key_number in no_repeat_number_list:
		aux_list = []
		for word in no_repeat_list:
			if len(word) == key_number:
				aux_list.append(word)
			aux_list.sort()
		dictionary[key_number] = aux_list

	return dictionary
###Part 4: Final grad Calculation
def my_final_grade_calculation(filename):
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    
    no_return_list = []
    for item in data:
        no_return_list.append(item.strip('\n'))

    no_spaces_list =[]
    for item in no_return_list:
        no_spaces_list.append(item.replace(' ',''))

    list_of_lists = []
    for x in no_spaces_list:
        list_of_lists.append(x.split(','))
        
    #--------------------------------------------
    dictionary = {}
    
    for element in list_of_lists: #start running elements of list of lists
        sort_quizes = []
        sort_assignments = []

        for quiz in range(1,7): #get the values of quizes sorted less to more
            sort_quizes.append(int(element[quiz]))
        sort_quizes.sort()

        for assignment in range(7,11): #get the values of assginments sorted less to more
            sort_assignments.append(int(element[assignment]))
        sort_assignments.sort()

        max_quizes = sort_quizes[2:] #split the sort_quizes from position 2 to end
        max_assignments = sort_assignments[1:] #split the sort_assignment from position 1 to end
        midterm = int(element[11])
        final = int(element[12])

        #get the average of each student
        average = ((sum(max_quizes)/4)*.25) + ((sum(max_assignments)/3)*.25) + (midterm*.25) + (final*.25)
        average = "{0:5.2f}".format(average)

        if float(average) >= 60:
            dictionary[element[0]] ="pass"
        else:
            dictionary[element[0]] ="fail"

    return dictionary

### Part 5: MY_2D_LIST
def MY_2D_LIST(number):

	#first fill the 2d list without final values
	fill_list=[]	
	if number >= 1:
		for x in range(1, number+1):
			aux_list = []
			if x == 1:
				aux_list.append(1)
			else:
				for y in range(0, x):
					aux_list.append(1)
			fill_list.append(aux_list)

	#second make the logic to fill the 2d list with 
	#the desire values
	final_list =[]	
	for n in fill_list:
		if len(n) == 1 or len(n) == 2:
			final_list.append(n)
		else:
			for z in range(1, len(n)-1):
				change = final_list[-1][z] + final_list[-1][z-1]
				n[z] = change
			final_list.append(n)


	return final_list

#print(MY_2D_LIST(9)) 

