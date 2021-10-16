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
ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
 
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]
 
thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]
 
#n = input('please enter an integer between 1 and 999: ') 
def num999(n):
    c = n % 10 # singles digit
    b = ((n % 100) - c) / 10 # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit
    d = ((n % 10000) - (a*100)-(b * 10) - c) / 1000 # thousends digit
    m = ""
    t = ""
    h = ""
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
        h = twenties[b] + ones[c]
    st = m + t + h
    
    return st

    def num2word(n):
        if n == 0: return 'zero'
        i = 3
        n = str(n)
        word = ""
        k = 0
        while(i == 3):
            nw = n[-i:]
            n = n[:-i]
            if int(nw) == 0:
                word = num999(int(nw)) + thousands[int(nw)] + word
            else:
                word = num999(int(nw)) + thousands[k] + word
            if n == '':
                i = i+1
            k += 1
        print(word[:-1])
        return word[:-1]
"""









    








