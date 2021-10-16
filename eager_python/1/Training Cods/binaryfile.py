def main():
    buffersize = 200000
    infile=open('D:\Program Files\Python 3.82\IMG_2788.JPG','rb')
    outfile=open('D:\Program Files\Python 3.82\pic.jpg','wb')

    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('my pic',end=' ')
        buffer=infile.read(buffersize)
    print('    ')
    print("DONE done")
main()

print('\xff' )
# mishe injoori ham nevesht
#open('D:\Program Files\Python 3.82\IMG_2788.JPG','rb').read(40000)
#open('D:\Program Files\Python 3.82\pic.JPG','wb').write('D:\Program Files\Python 3.82\IMG_2788.JPG','rb').read(40000)
