from typing import Counter


def insetions_sort(arr:list) -> list:
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            continue
        else:
            for j in range(i ):
                if arr[j]> arr[i]:
                    temp = arr.pop(i)
                    arr.insert(j,temp)
                    break
    return arr
    


arr = [10,2,3,-1,30,2,3,-5,15,0]
print(arr)
print(insetions_sort(arr))
