def _reverse_of_a_list_sample_(old_list):
    "Make a revers list"
    new_list = []
    length = len(old_list)
    i = -1
    # Iterate the list using negative indices
    while i >= -length:
        new_list.append(old_list[i])
        i = i - 1
    return new_list


some_list=[5, 6, 8, 9, 'PYTHON','PYTHON', 9, 8, 6, 5]
def crazy_list(some_list):
    " comapare some_list by reversed some_list"
    def _reverse_of_a_list_sample_(some_list):
        new_list = []
        length = len(some_list)
        i = -1
        # Iterate the list using negative indices
        while i >= -length:
            new_list.append(some_list[i])
            i = i - 1
        return new_list
    dd=_reverse_of_a_list_sample_(some_list)
    print(dd)
    print(some_list)
    if dd == some_list:
        return True
    else:
        return False
    


cc=crazy_list(some_list)

    
