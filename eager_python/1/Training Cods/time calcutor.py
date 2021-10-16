class time:
    def __init__(self,h=0,m=0,s=1):
        self.h= h 
        self.m= m 
        self.s= s 

    def show(self):
        return print(h , ':' ,m ,':',s)
    def str(self):
        return str(str(h , ':' ,m ,':',s))
    def __add__(self,other):
       

        if self.s + other.s >= 60:
            self.m +=1
            s= self.s+other.s -60
            print((self.h + other.h) ,(self.m+ other.m) , s)
        else: pass
        if self.m + other.m>= 60:
            self.h +=1
            m = self.m + other.m -60
            print((self.h + other.h) ,m , s)
        else:
            return (self.h + other.h) ,(self.m+ other.m) , (self.s + other.s)
        
 #   def __sub__(self,other):
  #      return (self.h - other.h) ,(self.m - other.m) , (self.s - other.s)

    

t1 = time(7,16,10)
t2 = time(3,30,35)

print(t1 + t2)
#print(t1-t2)

