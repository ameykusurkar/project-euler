import math

def largest_prime_factor(n):
    sqrt_n = int(math.sqrt(n))
    for i in reversed(range(sqrt_n)):
        if prime_factor(n, i):
            return i

def prime_factor(n, i):
    return factor(n, i) and is_prime(i)

def factor(n, i):
    return n % i == 0

def is_prime(i):
    for attempt in range(2, int(math.sqrt(i)) + 1):
        if i % attempt == 0:
            return False

    return True

print(largest_prime_factor(600851475143))
