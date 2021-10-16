def main():
    try:
        for line in readfile('text2.txt'): print(line.strip())
    except IOError as e:
        print('coud not open file',e)
    except ValueError as e:
        print('bad file name',e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError ('wrong file extenion')

if __name__ == '__main__':main()

 #you can see mor document in https://www.doc.python.org/3/library/exception.html