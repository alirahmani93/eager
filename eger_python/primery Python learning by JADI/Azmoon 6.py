MY_LIST = [['mean', 'really', 'is', 'jean'], ['world', 'my', 'rocks', 'python']]
### Part 2:
def list_to_tuples(MY_LIST):
    final_tuple=[]
    for lists in MY_LIST:
        lists.reverse()
	final_tuple.append(tuple(lists))
	return tuple(final_tuple)
### Part 3:

def calculate_grades(filename):
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()

    no_return_list = []
    for item in data:
	no_return_list.append(item.strip('\n'))
    list_of_lists = []
    for x in no_return_list:
	list_of_lists.append(x.split(','))
    #-----------------------------------------
    final_tuple = []
    for z in list_of_lists:
        aux_list = []
        sum_index = 0
        aux_list.append(z[0])
        for x in z[1:]:
            sum_index += int(x)
        aux_list.append(sum_index/4)
        final_tuple.append(tuple(aux_list))

    final_tuple.sort()
    return tuple(final_tuple)

### part 4:
argument = {'vader': 40, 'troy': 84.5, 'puma': 98.5, 'darth': 78.9, 'kevin': 88.454}
def formatted_print(arguments):

    values_list= list(arguments.values())
    values_list.sort()
    values_list.reverse()

    for value in values_list:
        for argument in arguments:
            if arguments[argument] == value:
                print("{0:10s}{1:6.2f}".format(argument, value))

### Part 5:
def calculate_expenses(filename):
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
    #-----------------------------------------------
    products_names_list = []
    for product in list_of_lists:
        if product[0] not in products_names_list:
            products_names_list.append(product[0])
    products_names_list.sort()

    expenses_list = []
    for name in products_names_list:
        sum_prices = 0
        aux_list = []
        for item in list_of_lists:
            if item[0] == name:
                sum_prices += float(item[1])
        aux_list.append(name)
        aux_list.append("${:.2f}".format(sum_prices))
        expenses_list.append(tuple(aux_list))

    return expenses_list
