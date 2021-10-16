def main():
    def multiplication(numbers,a=1):
        for i in numbers: a*=i
        return a

    def add(numbers,a=0):
        for i in nembers:a+=i
        return(a)

    def divide(numbers,a=1):
        a=numbers[-1]
        for i in range(len(numbers)-1):
            a/=numbers[-2]
            del numbers[-1]
        return a

    def minus(numbers): return numbers[0]-numbers[1]
    def power(numbers): return( numbers[0]**numbers[1])
    def power2(numbers):return( numbers[0]**2)
    def sqrt(numbers):return( numbers[0]**0.5)
    def log10(numbers):
        import math
        result=[]
        for i in range(len(numbers)):
            result.append(math.log10(numbers[i]))
        return result

    def perX(numbers):
        result=[]
        for i in range(len(numbers)):
            result.append(1/numbers[i])
        return result

    def factorile(numbers):
        result=[]
        for num in numbers:
            a=1
            for i in range(1,num+1):a*=i
            result.append(a)
        return result
    def fibonanchi(numbers):
        class Fibo():
            def __init__(self,a,b):
                self.a=a
                self.b=b

            def series(self):
                while True:
                    yield (self.b)
                    self.a , self.b=self.b , self.a +self.b

        f= Fibo(0,1)
        x=numbers[0]
        for r in f.series():
            if r>x: break
            print (r)
            
    ##
    count_number= int(input("numbers count: "))
    numbers=[]
    for i in range(count_number):
        n=int(input("number {} is: ".format(i)))
        numbers.append(n)
    ##
    oprators={0:multiplication ,1:add ,2:divide ,3:minus,4:power, 5:power2,
              6:sqrt, 7:log10,8:perX, 9:factorile,10:fibonanchi}
    print("""oprators list is 0:multiplication, 1:add, 2:divide, 3:minus, 4:power,
                 5:power2, 6:sqrt, 7:log10, 8:perX, 9:factorile, 10:fibonanchi""")

    opNum=int(input("what do you want to do: ")) 

    xx=print(oprators[opNum](numbers))
if __name__ == '__main__':main()
