#def main():
#    testfunc(5,6,3,9,8,15,4, one=10, two=20)
#def testfunc(*args,**kwargs):
#    for k in kwargs:print(k)
#if __name__ == '__main__':    main()

def main():
    print(testfunc())
    for i in testfunc():
        print(i,end=', ')
def testfunc():
    return range(1,20)

if __name__ == '__main__':    main()