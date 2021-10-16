def main():

    fin = open('D:/Program Files/Python 3.82/text.txt' , 'r', encoding='utf_8')
    fout = open('D:/Program Files/Python 3.82/text.html','w')
    outbytes= bytearray()
    for line in fin:
        for c in line:
            if ord(c)>127 :
                outbytes += bytes('&#{:04dict};'.format(ord(c) , encoding = 'utf_8'))
            else:outbytes.append(ord(c))
            outstr = str(outbytes,encoding='utf_8')
            print(outstr,file=fout)
            print(outstr)
            print('Done')
main()