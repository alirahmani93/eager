#inheritance

class animal:
    def talk(self) :print('talk loader')
    def walk(self) :print('hey walk faster')
    def clothes(self): print('i want nice clothes')


class Duck(animal):

    def quak(self):
        print('quuaaak')

    def walk(self) :
        super().walk()
        print('wlks like duk')
#python's objects don't care what the name of class is !!
def main():
    donald=Duck()
    donald.quak()
    donald.walk()
    donald.clothes()
if __name__ == '__main__':
    main()

