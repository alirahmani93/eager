def isprime(m):
    if m == 1:
          return False
    for x in range(2, m):
        if x % m == 0:
            return False
    else:
         return True

def primes ( m= 1 ):
     while True :
        if isprime(m): yield m
        m += 1

for m in primes():
     if m < 100: break
     print(m)
