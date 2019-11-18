from math import sqrt
from itertools import count
from utils import timeit

def triangle(n):
    return n * (n + 1) // 2

def num_factors(n):
    result = 1
    for i in range(1, int(sqrt(n) + 1)):
        quotient, remainder = divmod(n, i)
        if remainder == 0:
            result += 1
            if i != quotient:
                result += 1
    return result

@timeit
def run():
    for i in count():
        tri = triangle(i)
        result = num_factors(tri)
        if result > 500:
            return tri

print(run())
