def reverse_string_v1(s):
    r=''
    for char in s:
        r= char + r
        #print("r is: {} \n char is: {}".format(r,char))
    return r

def reverse_string_v2(s):
    r=''
    for i in range(len(s)-1,-1,-1):
        #print(i)
        r+=s[i]
    return r

    
my_string=input("your string: ")
cc= reverse_string_v1(my_string)
zz= reverse_string_v2(my_string)
