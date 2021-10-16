class   animalactions:
    def quak(self):return self.strings['quak']
    def feathers(self):return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']
class   Duck(animalactions):
    strings = dict (
        quak = "quak",
        feathers = "the duck is gray",
        bark = "duck can not bark",
        fur = "the duck has no fur"
    )
class Dog(animalactions):
    strings = dict (
        quak="dog can not quak!!",
        feathers="the Dog has no feathers",
        bark="HOP Hop",
        fur="the dog has white fur and green spots"
    )


def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quak)
    print(duck.feathers())

def main():
    fuck = Duck()
    milo =Dog()
    print("in the dog House")
    for o in (fuck, milo):
       in_the_doghouse(o)
    print('in the forest: ')
    for i in (fuck, milo):
          in_the_forest(i)


if __name__ == "__main__" : main()



