""""
sharjeri darim k ba st. amrica be sooorate 3 shakhe ast va ma inja to iran ba yek tabdili be 2 shakhe tabdil mikonim
"""
from abc import ABC,abstractmethod

class Target(ABC):
    @abstractmethod
    def operation(self):
        pass

class Adaptee:
    def specific_operation(self):
        return "2 Shakhe"
class Adaptee2:
    def specific_operation2(self):
        return "3 Shakhe"
class Adaptor(Target,Adaptee):
    def operation(self):
        print(f"{self.specific_operation()}")

class Adaptor2(Target,Adaptee2):
    def operation(self):
        print(f"{self.specific_operation2()}")


    def plugin(self):
        return True
    # def Operation(self):
    #     print('220v to 18v')
    #
    # def specific_operation(self):
    #     print("do shakhe")

def Client(Target):
    Target.operation()

if __name__ == "__main__":
    plug = Adaptor()
    adpt = plug.adaptee.specific_operation()
    tar  = plug.target.operation()