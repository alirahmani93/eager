class Duck:
    def __init__(self,**kwargs):
        self.properties  =kwargs
    def quak(self):
        print('quak')
    def walk(self):
        print('like Duck')
    def get_properties(self):
        return self.properties
    def get_property(self,key):
        return self.properties.get(key , None)
    @property
    def color(self):
        return self.properties.get('color',None)
    @color.setter
    def color(self,c):
        self.properties['color']=c
    @color.deleter
    def color(self):
        del self.properties['color']
def main():
    donald=Duck(color = 'red')
    donald.color = input('??? ')
    print(donald.get_property('color'))

if __name__ == '__main__':
    main()