from math import sqrt

def largest_prime_factor(n):
    sqrt_n = int(sqrt(n))
    for i in reversed(range(sqrt_n)):
        if prime_factor(n, i):
            return i

def prime_factor(n, i):
    return n % i == 0 and is_prime(i)

def is_prime(i):
    return not any(i % attempt == 0 for attempt in range(2, int(sqrt(i)) + 1))

print(largest_prime_factor(600851475143))
