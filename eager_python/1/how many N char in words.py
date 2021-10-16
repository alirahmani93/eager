def nwis(string, n):   #nwis = n_word_in_Str
    number_of_n_words=0
    words=string.split()
    for word in words:
        if len(word)==n:
            number_of_n_words+=1
    return number_of_n_words

string=input("your string is: ")
#n=int(input("tour n is: "))
for n in range (1,10):
    print( "number of: {} \t word is {}".format(n, nwis(string, n)))
cc=nwis(string, n)
