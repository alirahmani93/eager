def main():
    #infile = open('filename, 'rt' or 'a'==append or 'r+' == 'r' and 'w' or 'rb' == read bynery)
    infile = open('D:/Program Files/Python 3.82/text.txt', 'r')
    outfile = open('D:/Program Files/Python 3.82/new.txt', 'w')
    for line in infile:
        print(line,file=outfile,end=' ')
    print('done')

    buffersize = 10000
    infile2= open('D:/Program Files/Python 3.82/bigfile.txt', 'r')
    outfile2=open('D:/Program Files/Python 3.82/new bigfile.txt', 'w')
    buffer = infile2.read(buffersize)
    while   len(buffer):
        outfile2.write(buffer)
        print('.10k',end='  ')
        buffer=infile2.read(buffersize)

    outfile2.write('enddddddddddd')
    print()
    print('Done')

main()

