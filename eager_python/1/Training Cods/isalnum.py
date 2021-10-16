"""""
s= 'this is sTRIng      '
m='thisisstringw44444hitoutspaces'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.strip())
print(s.rstrip())
print(s.replace('this is','those are'))
print(s.find('is'))
print(m.isalnum())
print(m.isalpha())
print("123456".isdigit())
print('458569'.isnumeric())
"""""
a,b=10 , 21
print(a,b)
s= 'this is {}, that is {}' ; print(s)
print(s.format(a,b))
print(id( s))
new= print(s.format(a,b))
print(id(new))
print('this is %d, that is %d'%(a,b))
print('this is {1}, that is {0}'.format(a,b))
print('this is {0}, that is {0} and this is too is {1}'.format(a,b))
print('this is {bob} and thst is {fred}'.format(bob=a , fred=b))

d=dict(bob=a*1.5 , fred=b*3.14)
print('this is {bob} and thst is {fred}'.format(**d))  # ** hr moghe didim yani dictionary