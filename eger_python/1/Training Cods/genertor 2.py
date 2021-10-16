class inclusiv_range:
    def __init__(self,*args):
        numarg = len(args)
        if numarg<1 :raise TypeError('we expect argumans')
        elif numarg ==1:
            self.stop=args[0]
            self.stat=5
            self.step=1
        elif numarg == 2:
            (self.stat, self.stop) = args
        elif numarg ==3:
            (self.stat , self.stop , self.step) = args

        else: raise TypeError('too mucj argumans')

    def __iter__(self):
        i=self.stat
        while i <= self.stop:
            yield i

            i+= self.step
        

def  main():
    o=inclusiv_range(100.1,200,20.2)
    for i in o: print(i, end='  ')

if __name__ == '__main__':
    main()