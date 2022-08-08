def quick_sort(arr:list):
    left , right = [] , [] 
    # if len(arr) ==1:
    #     return arr[0]
    if len(arr)>1:
        pivot = arr.pop()
        for elm in arr:
            if elm >=  pivot:
                right.append(elm)
            else: 
                left.append(elm)

        left = quick_sort(left)
        right = quick_sort(right)
        result= left + [pivot] + right
        return result
    return arr

array = [10, 7,0, 8, 9, 1, 5]
quick_sort(array)


"""
# def part(arr):
#     leng        = len(arr)
#     pick_len    = leng // 2
#     pick        = arr[pick_len]
#     arr.pop(pick_len)
#
#     right, left = list(), list()
#
#     print("PICK: ", pick)
#     for i in arr:
#         if pick < i:
#
#             right.append(i)
#             # arr.pop()
#         else:
#             left.append(i)
#     m = part(left)
#     return print("M: ", m)#"LEFT: ", left, "RIGHT:", right )
#
# def quick_sort(start, end ,arr):
#
#     partition = part(start, end, arr)
#
#     quick_sort(start,partition, arr)
#     quick_sort(partition, start, arr)
#
#
# arr = [10,12,0,40,20,50,30,15]
# end =len(arr)
# start = 0
# print("Array: ",arr)
# quick_sort(start, end, arr)

#_____________________
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# Driver code"""

#  quick_sort(0, len(array) - 1, array)

# print(f'Sorted array: {array}')