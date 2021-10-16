class Duck:
    def talk(self): print('talk loader')
    def walk(self): print('hey walk like a duck')
    def clothes(self): print('i want nice clothes')
class Dog():
    def talk(self): print('Hop hop')
    def walk(self): print('walk by hand and feet')
    def clothes(self): print('black and white fur')

def main():
    donald = Duck()
    milo = Dog()
    in_the_forrst(donald)
    in_the_house(milo)
def in_the_forrst(num1):
    num1.talk()
    num1.walk()
def in_the_house(num2):
    num2.talk()
    num2.clothes()
main()