def main():

    fh = open("D:/Program Files/Python 3.82/text.txt")
    for line in fh.readlines():
        print(line,end='   ')
if __name__ == '__main__':main()