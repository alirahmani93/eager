# Method 1

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if x % n == 0:
            return False
    else:
        return True

        def primes(n= 1):
            while (True):
                if isprime(n): yield (n)
                n += 1

        for n in primes():
            if n > 100:yield
            print(n)
# Method 2

def check_prime_sample_(n):
    if n < 2:
        return False
    # Iterate from 2 to the number
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
