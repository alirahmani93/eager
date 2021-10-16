class   animalactions:
    def quak(self):return self.strings["quaaak Quaaak"]
    def feathers(self):return self.strings["Feathers"]
    def bark(self): return self.strings["bark"]
    def fur(self): return  self.strings["fur"]
class   Duck(animalactions):
    strings = dict (
        quak = "QUAAAAK!!",
        feathers = "the duck is gray",
        bark = "duck can not bark",
        fur = 'the duck has no fur'
    )
class Dog(animalactions):
    strings = dict (
        quak="dog can not quaak!!",
        feathers="the Dogha has no feathers",
        bark="HOP Hop",
        fur='the dog has white fur and green spots'
    )
def in_the_doghouse(Dog):
    print(Dog.bark())
    print(Dog.fur())
def in_the_forest(Duck):
    print(Duck.quak)
    print(Duck.feathers())
def main():
    donald =Duck()
    milo =Dog()

    print('in the forest: ')
    for o in(donald , milo):
        in_the_forest(o)
    print("in the dog House")
    for i in (donald , milo):
        in_the_doghouse(i)
