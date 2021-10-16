def _merge_and_sort_sample_(a, b):
    a.extend(b)
    # Create a new list
    new_list = []
    # Loop until a becomes empty
    while a:
        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = a[0]
        # loop through the list and
        # find the element that is smallest
        for element in a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)
        # now remove that smallest element from the original list
        a.remove(maximum)   # if we don't remove A, loop never stopped
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list
