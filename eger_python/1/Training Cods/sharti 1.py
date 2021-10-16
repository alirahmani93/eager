def main():
    a,b=4,1
    print("a<b") if a<b else print("a!<b")

    if a<b:
        print ('a<b')
    elif a>b:
        print ("a>b")
    else:
        print("a=b")

if __name__ == '__main__':main()