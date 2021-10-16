def get_primes(n):  # n = max_num
     # +++your code here+++
    list1 = []
    if n==2:
     list1.append(2)
    for y in range(2, n):
     for x in range(2, y):
         if y % x == 0:
             break
     else:
         list1.append(y)
    return list1

