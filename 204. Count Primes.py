# all primes <= sqrt(n) 
# this would be o(n) operation 
# number of combinations, resulting in products <= n 
# ans is n - this  number 

from math import sqrt, ceil



def get_primes(n): 
    res = [2] 
    for i in range(3, n + 1, 2): 
        isPrime = True  
        for prime in res: 
            if i % prime == 0: 
                isPrime = False 
                break
        if isPrime: 
            res.append(i)
    return res 


def solver(n): 
    n -= 1
    if n < 2: 
        return 0 
    primes = get_primes(ceil(sqrt(n)))
    not_prime = set() 
    for prime in primes: 
        for i in range(2 * prime, n + 1, prime): 
            not_prime.add(i)
    return n - 1 - len(not_prime)



print(solver(7))