def find_gcd(some_list):
    greatest_div = 0
    lowest_element = min(some_list)
    for i in some_list :
        if i%lowest_element == 0 :
            print(lowest_element)
            if lowest_element == greatest_div :
                greatest_div = 1
            else :
                greatest_div = lowest_element
    return(greatest_div)

my_list_a = [12, 24, 6, 18]
#my_list_a = [3, 5, 9, 11, 13]
my_gcd = find_gcd(my_list_a)

print(my_gcd)
