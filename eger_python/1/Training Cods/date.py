day=int(input('day'))
days=range(1,32,1)
if day not in days: print('Out of Range',day,sep=":")
month=int(input('month'))
year=int(input('year'))



daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
result=0
if year%400 ==0:
    daylist[1]=29
    print('Kabise year')

if month>1:
    for dayspassed in daylist[:month-1]:
        result +=dayspassed
else:  result=0
print(result + day)