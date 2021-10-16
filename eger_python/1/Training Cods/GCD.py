#mid term q.9
#some_list=[3, 5, 9, 11, 13]
"""some_list=[12, 24, 6, 18,34]

max_num= max(some_list)
def get_primes(max_num):  # n = max_num
     # +++your code here+++

    list1 = []
    if max_num==2:
     list1.append(2)
    for y in range(2, max_num):
     for x in range(2, y):
         if y % x == 0:
             break
     else:
         list1.append(y)
    return list1

zz=get_primes(max_num)
def find_gcd(some_list):
    B=max_num= max(some_list)
    a = []
    b = min(some_list)
    for k in zz  :
        for i in some_list:
            if i%k==0:
                a.append(i)
    return a

cc=find_gcd(some_list)
"""

import math
some_list=[12, 24, 6, 18,34]
Min =min(some_list)
for i in some_list:
    Min = math.gcd(Min, i)
print(Min)