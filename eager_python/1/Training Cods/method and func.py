class duck:
    def __init__(self,value="none" ,value2=0):          #constractor
        self._v= value
        self._v2=value2
    def quak(self):                                     # Method
        print('quaaak!',self._v,self._v2)
    def walk(self):                                     # Method
        print('walks like duck',self._v,self._v2)

def main():                                             #funcion
    donald = duck(5,4)              #assign to calss
    sajad = duck(value2=20)
    donald.quak()
    sajad.quak()
    donald.walk()
    sajad.walk()

if __name__ == '__main__':
    main()
