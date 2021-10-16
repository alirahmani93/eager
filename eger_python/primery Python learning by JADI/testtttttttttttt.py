"""
a= int(input("ye add bein 1 ta 7 begoo"))

weekdays=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY",
          "FRIDAY","SATURDAY","SUNDAY"]
print(weekdays[a-1])
"""
"""
string =str(input("whats your strig: "))
if 'dog' in string:
    print("Yes")
else: print("No")
"""
"""  
number =int(input("whats your number: "))
if number %3==0:
    print("Yes")
else: print("No")
"""
"""
if False:
    print('false')
elif 2**3 == 8 :
    print('true')
else:
    print('none')
"""
"""
my_string="hello"
if 10 % 5:
    print('true')
elif "le" not in my_string :
    print('false')
else:
    print('none')
"""
"""
x = 100
if x > 10 :
    x = x + 10
if x > 20 :
    x = x + 50
print(x)#160
"""
"""
string =str(input("whats your strig: "))

if "dog" in string:                     print("Dog")
elif  "cat" in string:                  print("Cat")
else:                                   print("None")
"""
"""
number =int(input("whats your number: "))
if number == 2:     print("two")
elif number == 3:   print("three")
elif number == 5:   print("five")
else:               print("other")
"""
"""
x == 0
print(not x) #Error
"""
"""
a = 14 // 3
b = 4 > 5
print( a and b)
"""
"""
my_list = [ 'dog', 'cat', 'worm', 2.3]
if 'doc' in my_list:
    my_list[1] = 4
else:
    my_list[2] = 6
print (my_list[1],my_list[2])
"""
"""
x = 4
if "z" in "computer science":
    x = x + 10
elif 5 % 3 == 2:
    x = x + 18
elif 5>4:
    x = x + 30
else:
    x = x + 5
print (x)
"""
"""
x = "c"
y = 3
if "x" in "computer science":
    y = y + 5
else:
    y = y + 10
if x in "computer science":
    y = y + 20
else:
    y = y + 40
print (y)
"""
"""
x = "python course"
print("cours" not in x )
"""
"""
age =int(input("whats your age: "))
if age<=0:                   print("UNBORN")
elif age>0 and age<=150:    print("ALIVE")
else:                       print("VAMPIRE")
"""
"""
num =int(input("whats your age: "))
if num%6==0 :                   print("BOTH")
elif num % 2==0 or num%3==0:    print("ONE")
else:                           print("NEITHER")
"""
"""
n =int(input("n: "))
r=list(range(n+1))
if n>=0 and n<=40:
    s=r[n]*8
    print("YOU MADE {} DOLLARS THIS WEEK".format(s))
#    print(s)
elif n>=41 and n<=50:
     s=40*8
     m=r[n-40]*9
     print("YOU MADE {} DOLLARS THIS WEEK".format(s+m))
     #print(s+m)
elif n>=51 and n<=168:
    s=40*8
    m=10*9
    n=r[n-50]*10
    print("YOU MADE {} DOLLARS THIS WEEK".format(s+m+n))
    #print(s+m+n)
else:print("INVALID")

"""
"""
n =int(input("give n: "))
day=n//86400
re=n%86400

h=re//3600
re2=re%3600

m=re2//60

s=re3=re2%60

print("{} days {} hours {} minutes {} seconds".format(day,h,m,s))
"""
"""
Factoriel =int(input("give number: "))
n=1
while Factoriel>0:
    n = Factoriel * n
    Factoriel -= 1
print(n)
"""
"""    
x = 1
count = 0
while x < 1001:
    count = count +x
    x = x + 3
print(count)
"""
"""
z=0
b=list(range(1,101))
for x in b:
    if x%2==0:z +=x
print(z)
"""
"""
n=int(input("n: "))
c=0
for i in range(1,n+1): c+=i
print(c)
"""
"""
n=int(input("n: "))
c=0
for i in range(1,n+1):
    v=i**2
    c+=v
print(c)
"""
"""
n=int(input("n: "))
c=0
for i in range(0,n+1):
    v=10**i
    print(v)
"""
"""
count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
print(count)
"""
"""
k = 1
while k<5:
    if k % 7 == 0:
        break
    k = k + 2
print(k)
"""
"""
my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    if element == "cat":
        continue
    count = count + 1
print(count)
"""
"""
my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)
"""
"""
my_str = "university"
count = 0
for char in my_str:
    count = count + 1
    if char == "e":
        break  
print(count)
"""
"""
m = 0
for x in range (1,3):
   for y in range (4,6):
      m = m + x + y
print (m)
"""
"""
m = 0
for x in range (1,3):
   k = 0
   for y in range (-2,0):
      k = k + y
      m = m + k
print (m)
"""
"""
m = 0
x = 1
while x < 4:
    y = 1
    while y < 3:
        m = m + x + y
        y = y + 1
    x = x + 1
print(m)
"""
"""
m = 0
x = 1
while x < 4:
    y = 1
    while y < 5:   
        m = m + y
        y = y + 1
        if x + y == 5:
            break
    x = x + 1
print (m)
"""
"""
m = 0
x = 10
while x > 8:
    for y in range(1,3):
        m = m + 1
    x = x - 1
print(m)
"""
"""
m = 1
for x in [1,2,3]:
    for y in [3,1,4]:
        if x == y:
            m = m * x 
print (m)

m = 1
my_list_1 = [2 , 4, 1]
for x in my_list_1:
    for y in range(1,3):
        if (x + y) % 3:
            m = m * x
print (m)

m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)
"""
"""
def say_hello(name):
    print("Hello {} !".format(name))

for i in ['ali','yasaman' , 'fatemeh', 'maman', 'reza']:
    say_hello(i)
"""
"""
#pow
x,y=5,3
p=pow(x,y)
print(p)    #125
"""
"""
def a(k):
    k+=5
    return print(k)
i= int(input('i: '))
a(i)
"""
"""
def zarb(a,b):
    r=a*b
    return r
"""
"""
def zarb(a,b):
    s=a*b
    p= 2*(a+b)
    return [s,p]
"""
"""
def _find_sum_sample_(sample_list):
    
    my_sum = 0
    
    for item in sample_list:
        
        my_sum = my_sum + item
    return my_sum

def a(m):
    x=0
    for i in m:
        x+=i
    return x
"""
"""
def avrage(a):
    x=0
    count=len(a)
    for i in a:
        x+=i
    
    avr=x/count
    return avr

def _average_sample_(sample_list):
    # Initialize total_sum to 0
    total_sum = 0
    number_of_elements = len(sample_list)
    
    for item in sample_list:
        
        total_sum = total_sum + item

    average = total_sum / number_of_elements
    
    return average

"""
"""
def max(a):
    maxx= a[0]
    for i in a:
        if i > maxx:
            maxx= i
    return maxx
"""
"""
def Y(x,y,z):
    y=x**2+y**2+z**2
    y**=.5
    return y

def D(vector):
    x= vector[0]
    y= vector[1]
    z= vector[2]
    d=x**2+y**2+z**2
    d**=.5
    n_x=x/d
    n_y=y/d
    n_z=z/d
    unit_vector=[n_x,n_y,n_z]
    return unit_vector
"""
"""
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[ 1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]
y = [0, 1]  # classes of each sample
clf.fit(X, y)
clf.predict(X)  # predict classes of the training data

clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create a pipeline object
pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=0)
)

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# fit the whole pipeline
pipe.fit(X_train, y_train)


# we can now use it like any other estimator
accuracy_score(pipe.predict(X_test), y_test)
"""
"""
k = 10
while k > 2:
    x = k / 2
    k = k - 1
print(x)

count = 0
for x in range(2,5):
    count = count + x
print(count)

count = 10
for x in range(0,7):
    count = count + 2
    if x == 4:
        break
print(count)

k = 1
count = 0
while count < 10:
    if k % 4 == 0:
        break
    count = count + k
    k = k + 1
print(count)

my_list = ["pet" ,"dog", 35, "cat", 23]
count = 0
for item in my_list:
    if type(item)== str:
        continue
    count = count + 1
print(count)

m= 0
my_str= "mississipi"
for char in my_str:
    if char == "s":
        continue
    if char == "p":
        break
    m = m +1
print(m)

m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print (m)

m = 0
x = 1
while x < 5:
    y = 1
    while y < 4:
        m = m + y
        y = y + 3
    x = x + 2
print(m)

m = 0
my_list_1 = [1, 2, 5]
my_list_2 = [1, 3, 2, 6, 5]
for x in my_list_1:
    for y in my_list_2:
        if x == y :
            m = m + 1
print (m)

m = 0
my_str_1 = "cat"
my_str_2 = "pet"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 1
#print(m)
#def fun(x, y, z): 
#    z = x * y
#    return x + y + z
#print(fun(2, 30))#Error

def fun1(x,y):
   z = multiply(x,y)
   m = x + z
   return m
  
def multiply(a,b):
   n = a * b
   return n
  
x = 2
y = 4
z = fun1(x,y)
print (x,y,z)

def my_fun(x):
    for m in range(0,3):
        n = 2
        while n <= 4:
            if m == n:
                x = x + 1
            n = n + 1
    return x
print(my_fun(5))
def myFun():
    count = 0
    for x in range (0,3): 
        count = count + x
    return 
print(myFun())

def find_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
find_max(3, 4)
def func(x):
    x = 2
    print('x is', x)
func(50)
"""
"""
n=int(input("n: "))
for i in range(n+1): print("*"*i)
for i in range(n-1,0,-1): print("*"*i)
"""
"""
def abc(z):
    z=[2,5,7,10,96,8,23]
    s =0
    for i in z:
        if i%2 !=0: s+=i
    return s
"""
"""
def perfectNumber(n):
    s=0
    b=range(1,n)
    for i in b :
        if(n%i==0):
            s+=i
    if (n==s):
        return True
    else:return False
a=perfectNumber(2**12*(2**13-1))
print(a)
"""
"""
number = int(input("Number :"))
def control(number):
    i = 2 
    if number <=1: return False
    
    while i*i<=number: 
        if number%i==0 : 
            return False
        i +=1 
    else:
        return True
print(control(number))
"""
"""
def LCM(a,b):
    s=a*b
    for i in range(1,s):
        A= s%i==0
        B= s%i==0
        
       if a%i==0 and b%i==0:
           return T
"""
"""
input_list = ["we", "love", "python", "so","much"]
def _every_other_element_sample_(sample_list):
    output = []
    length = len(sample_list)
    output.append(sample_list[0])
    for element in range(1, length):
        if element % 2 == 0:
            output.append(sample_list[element])
    return output
"""
"""
a = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
s = "Brahman"

def ex(a, s):
    for i in range(1, 4):
        a[i] = s
    return a
###

def ezaf(A,B):
    r=A+B
    return r
"""
"""
a,b=[1,3,2],[5,6,1]
def _custom_bubble_sort_sample_(original_list):
    # This is an implementation of the
    # famous bubble sort algorithm
    # This can a very inefficient algorithm
    # when used with large data
         
    # our purpose here however is to show how to sort
    # a list without any built-in methods
	

    # make a copy of the original list
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list

"""
"""
def _merge_and_sort_sample_(a, b):
    a.extend(b)
    # Create a new list
    new_list = []
    # Loop until a becomes empty
    while a:
        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = a[0]
        # loop through the list and
        # find the element that is smallest
        for element in a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)
        # now remove that smallest element from the original list
        a.remove(maximum)
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list

def count_mylist(a,b):
    d=0
    for element in a:
        if element == b:
            d+= 1
    return d
        
def my(x):
    x.pop(0)
    x.pop()
    return x

def sample7 (a):
    mylist=a[:]
    for i in range(len(a)):
         if a[i] %2 !=0:
             mylist[i]+=1
         return mylist

def sample7(a):
    mylist = a[:]
    for x in range(0, len(mylist)):
        if mylist[x] % 2 != 0:
            mylist[x] +=1
    return mylist

def sum_of_evens_sample(a,b):
    c=a+b
    total=0
    for x in c:
        if x % 2 != 0:
            total += x
    return total

def sample9(a):
    x=[]
    for item in a:
        if item not in x:
            x.append(item)
    return x


def sample10(a,b):
    a.extend(b)
    x=[]
    for item in a:
        if item not in x:
            x.append(item)
    return x

def _reverse_of_a_list_sample_(old_list):
    new_list = []
    length = len(old_list)
    i = -1
    # Iterate the list using negative indices
    while i >= -length:
        new_list.append(old_list[i])
        i = i - 1
    return new_list
"""
# Mid term q.1
"""
x = ["dog", 2, "cat", 34, 5.8]
m = 0
for i in range(len(x)):
    m = m + i
print(m)

i = 1
while False:
    if i % 5 == 0:
        break
    i = i + 2
print(i)

count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print(count)

def my_fun(a):
    a[0] = 'new value:'     
    a[1] = a[1] + 1      

x = ['old value:', 99]
my_fun(x)
print (x[0], x[1])

x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0
for item in x:
    m = 0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print(count)

x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0
for item in x:
    m = 0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print(count)

x = 0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x = x + 1
print(my_list.count("dog"))

def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print ('my_fun: ',my_fun(y))

count = 0
my_list = [2, 4, 1, 5, 7, 3, 9, 4]
new_list = my_list[1:7:2]
for item in new_list:
    count = count + 1
print(count)

def my_fun(x,y):
    m = x ** y  
y = my_fun(2, 3)    
print(y)
"""
#<id term q.2
"""
my_list = []
for k in range(1,101,20):
    my_list.append(k)
print (my_list[: :2] )

def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun(m)
print(m)

def my_fun(x):
    for k in range (len(x)):
        x.append(x[:k])
m = [1,5,3]
my_fun(m)
print(m)

my_list = [9, 8, 7]
for k in range (3):
    my_list.insert(-k, k+1)
print(my_list)

my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    if k % 2:
        m = my_list.pop(k)
        new_list.append(m)
print(new_list)

def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)

def my_fun(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun(values)
print(values)

def my_fun(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x
 
values = [2, 9, 16, 3, 24, 13, 15]
print(my_fun(values))

def my_fun(i):
    values = []
    values.append(i)
    return values
my_fun(5)
print(my_fun(3))

# Mid term part q.3

input_list=[2, 9, 16, 3, 24, 13, 15]
def find_integer_with_most_divisors(input_list):
    counter_list = []
    for item in input_list:
        counter = 0
        for j in range(1, item+1):
            if item % j == 0:
                counter = counter + 1
        counter_list.append(counter)
    most_divisors_index = counter_list.index(max(counter_list))
    Integer_with_most_divisors = input_list[most_divisors_index]
    return Integer_with_most_divisors

               
xx=find_integer_with_most_divisors(input_list)
# Mid term part q.4
def list_of_primes (n):
     
    list = []
    if n==2:
     list.append(2)
    for y in range(2, n):
     for x in range(2, y):
         if y % x == 0:
             break
     else:
         list.append(y)
    return list

# Mid term q.5
a,b=[1,2,3],[800,700,600]
def items_price(a,b):
    
    p=0
    A,B=len(a),len(b)
    for i in range(A):
        for k in range(B):
            if i==k:
                
                p+= a[i]*b[k]
    return p

## Mid term q.6
some_list=[5, 6, 8, 9, 'PYTHON','PYTHON', 9, 8, 6, 5]
def crazy_list(some_list):
    def _reverse_of_a_list_sample_(some_list):
        new_list = []
        length = len(some_list)
        i = -1
        # Iterate the list using negative indices
        while i >= -length:
            new_list.append(some_list[i])
            i = i - 1
        return new_list
    dd=_reverse_of_a_list_sample_(some_list)
    print(dd)
    print(some_list)
    if dd == some_list:
        return True
    else:
        return False
    


cc=crazy_list(some_list)

# Mid term q.7
def pattern_sum(k, m):
    total = 0
    # Getting a range for Pattern
    for i in range(1, m + 1):
        # Logic
        i = (i * str(k))
        total += int(i)
    return total"""
"""
# Mid term q.8

def unique_common(a, b):
    x=[]
    z=[]
    for i in a:
        for k in b:
            if i==k: x.append(i)
    for item in x:
        if item not in z: z.append(item)
    if z==[] :return 'None'
    z.sort()
    return z
# Mid term q.9
some_list=[3, 5, 9, 11, 13]
def find_gcd(some_list):
    a = 0
    l = min(some_list)
    for i in some_list :
        if i%l == 0 :
            a=l
        else :
            a = l
    return(a)

## Mid term q.10
n=int(input('please enter an integer between 1 and 9999: '))

if n<10:
    if n==1: print('one')
    if n==2: print('two')
    if n==3: print('three')
    if n==4: print('four')
    if n==5: print('five')
    if n==6: print('six')

num = int(input('please enter an integer between 1 and 9999: '))
x=[]
#while (num):
#  print(int(num % 10))
#  num = int(num / 10)
#  x.append(num)
s=str(num)
for i in s:
    i=int(
    x.append(i)
"""
"""
n = int(input('please enter an integer between 1 and 9999: ') )
ones = ["", "one","two","three","four", "five", "six","seven","eight","nine","ten","eleven","twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen", "eighteen","nineteen"]
 
twenties = ["","","twenty","thirty","forty", "fifty","sixty","seventy","eighty","ninety"]
 
thousands = ["","thousand"]


c = n % 10 # singles digit
b = ((n % 100) - c) / 10 # tens digit
a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit
d = ((n % 10000) - (a*100)-(b * 10) - c) / 1000 # thousends digit
m = ""
t = ""
h = ""
j=" "
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if d!=0 and a != 0 and b == 0 and c == 0:
    m=ones[d] + " thosend"
elif d !=0:
    m = ones[d] + " thosend " #and
if a != 0 and b == 0 and c == 0:
    t = ones[a] + " hundred"
elif a != 0:
    t = ones[a] + " hundred " #and 
if b <= 1:
    h = ones[n%100]
elif b > 1:
    h = twenties[b] + j+ones[c]
st = m + t + h
print(m+t+h)
"""
"""
def coffee(n):
    m=[]
    for i in range(1,6):
        m.append(i*n)
    return m
def ev(a,b):
    m=[]
    for i in range(a,b):
        if i%2==0:
            m.append(i)
    return m

def odd(a,b):
    m=[]
    for i in range(a,b+1):
        if i%2!=0:
            m.append(i)
    m.sort(reverse=True)
    return m

def cube(k):
    m=[]
    for i in range(1,k):
        m.append(i**3)
    return m

def cube_root(k):
    m=[]
    for i in range(1,k):
        m.append(i**(1/3))
    return m
"""
"""
n =int (input("n: "))
x=1
while x<=n:
    
    print(x*str(x))
    x+=1

k =int (input("k: "))
for i in range(1,k+1):
    print(k*'*')
"""
"""
j=int (input("j: "))
if j>1:
    print(j*'*')
    for i in range(j-1, 1, -1):
        print('*'+(i-2)*' '+'*')
    print('*')
elif j==1:
    print('*')
    
n = int(input("Please enter a positive integer: "))
if n > 1:
    print (n*"*") # Print the top line
    for x in range(n-1, 1, -1):
        print("*"+ (x-2)*" "+"*") # Print the middle lines
    print("*") #print the bottom line
elif n == 1:
    print("*")
"""
def chik(a,b):
    # a is number and b is character
    A=chr(a)
    B=ord(b)
    return A , B
def ss(a):
    # Jame kole horof dar UTF-8
    c = 0
    for i in str(a):
        c+=ord(i)
        print(id(c))
    return c
x="oops too"
my_str = "oops too"
print (x.strip("o"))
print (my_str.lstrip('o'))
print (my_str.rstrip('o'))
print ("NO".join("test"))
print ( "test".join(["A","B","C"]))
