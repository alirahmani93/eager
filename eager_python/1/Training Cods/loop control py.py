def main():
    s='maybe this is a string'
    i=0
    for c in s:
        if c== 's':break
        print(c,end="")
    else:                   #boodo nabodesh farghi nadare
        print(c,end='')

    while   (i<len(s)):
        print(s[i])
        i+=3
    else: print ('smile')


if __name__ == '__main__':
    main()