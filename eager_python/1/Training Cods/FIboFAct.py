class Fibonachi():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def series(self):
        while True:
            yield (self.b)
            self.a , self.b=self.b , self.a +self.b

    f= Fibonachi(0,1)
    for r in f.series():
        if r>input(' ???  '): break
        print (r)


    def fact(r):
        if r ==1:
            return 1
        else:
            return arg*fact(r-1)
#class main(Fibonachi):
 #   return fact(f)
