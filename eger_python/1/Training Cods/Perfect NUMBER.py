def perfectNumber(n):
    #Perfect NUMBER
    s=0
    b=range(1,n)
    for i in b :
        if(n%i==0):
            s+=i
    if (n==s):
        return True
    else:return False
