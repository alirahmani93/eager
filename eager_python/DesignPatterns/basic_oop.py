#class Classname:
#    Attribute
#    method

#object oriented programming
#   1 inharitance
#    2 abstraction
#    3 encapsulation
#    4 polymorephysem

class Maschine:
    #Class Attrebiute= property :: variabe
    count=0
    
    def __init__(self,color,door_number,double_usage,sun_roof=False): # dunder method or magic method
        self.color = None
        self.door_number= None
        self.double_usage=None
        self.sun_roof=None
        self.tire_brand = 2 # for EX. Barrez
        Maschine.count+=1 #class attr ba esme khode class CALL mishe
    
    #@classmethod # khode __new()__ khoders defult class method hast pas decorator lazem nist
    def __new__(cls,*args,**kwargs):pass

    def __call__(self ):
        pass
    def __str__(self) -> str:
        return "ptint shode Object"
    #Method ::تابع
    def engine(self):
        pass
    def change_usage_sookht(self):
        self.double_usage
    def __partibazi(self):pass
    @staticmethod   #az yek method mamooli be yek static tabdil mishe va lazem nadare argument dashte bashe
    def company_time_work():
        print("sob ta shab")
    

class A:
    def __party():pass

class B(A):
    def test_private(self):
        print(self._A__party)
    def hello(self):
        print("hello in A")
    def hello():
        print("hello in B")
class C(B):
    def hello():
        super().hello() #az class pedar yek method miavard
        print("I am C")

#machine1= Maschine()
#machine1.engine()
as