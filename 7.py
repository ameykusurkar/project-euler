from math import sqrt
from itertools import count

def is_prime(n):
    return not any(n % i == 0 for i in range(2, int(sqrt(n)) + 1))

# All primes greater than 3 can be writen in the form 6k +/- 1
def attempts():
    yield 2
    yield 3
    for k in count(1):
        yield (6 * k) - 1
        yield (6 * k) + 1

def primes():
    return (n for n in attempts() if is_prime(n))

def get_prime(n):
    for i, prime in enumerate(primes(), 1):
        if i == n:
            return i, prime

print(get_prime(10_001))
