from math import sqrt
from itertools import count

def is_prime(n):
    return not any(n % i == 0 for i in range(2, int(sqrt(n)) + 1))

def primes():
    return (n for n in count(2) if is_prime(n))

limit = 10_001
for i, prime in enumerate(primes(), 1):
    if i == limit:
        print(i, prime)
        break
