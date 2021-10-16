class Duck:
    def __init__(self,**kwargs ):
        self.variables=kwargs

    def set_variable(self,k,v=None):
        self.variables[k]=v
    def get_variable(self,k=0):
        return self.variables.get(k,None)
def main():
    donald=Duck(feet=2,ali='reza ')
    donald.set_variable('color','red')

    print(donald.get_variable('color'))
    print(donald.get_variable('ali'))
    print(donald.get_variable('feet'))
    print(donald.get_variable('boo'))
if __name__ == '__main__':
        main()