import re

def main():
    fh = open("D:/Program Files/Python 3.82/text 2.txt")
    for line in fh:
        match = re.search("(re|dr)er",line)
        if match:
            print(match.group())
  #  for i in fh: print(i)
if __name__ == '__main__':
    main()
