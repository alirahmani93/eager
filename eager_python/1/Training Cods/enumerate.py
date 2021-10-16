def main():
    fh = open("D:/Program Files/Python 3.82/text.txt")
    #example 1
    for index,line in enumerate(fh.readlines()):
        print(index,line)

    #example 2
    s= "she is sousan"
    for i,c in enumerate(s):
        if c=='s':
            print('index {} is a {}'.format(i,c))


if __name__ == '__main__':
    main()