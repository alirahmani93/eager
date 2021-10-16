def BMM(a,b):
    while b>0:
        a,b=b,a%b
    return a

def KMM(a,b):
    return a*b/BMM(a,b)
def BMM_l(*nos):
    return reduce(BMM,nos)

def KMM_l(*nos):
    c= reduce(KMM,nos)
    return c

def KMM_lv2(*list_num):
    bb=1
    for i in range(len(list_num)):
        bb=KMM(list_num[i-1],bb)
    return bb
