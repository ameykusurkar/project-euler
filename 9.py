from utils import timeit

def is_triplet(a, b, c):
    return a ** 2 + b**2 == c**2

@timeit
def run():
    for c in range(1, 999):
        remaining = 1000 - c
        for b in range(1, remaining):
            a = remaining - b
            if a < b and b < c and is_triplet(a, b, c):
                return a * b * c

print(f"Answer: {run()}")
