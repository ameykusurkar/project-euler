from functools import reduce

def fact(n):
    return reduce(lambda acc, x: acc * x, range(1, n + 1), 1)

def is_digit_factorial(n):
    if n < 10:
        return False
    digits = map(int, str(n))
    return sum(fact(d) for d in digits) == n

result = list(filter(is_digit_factorial, range(int(5e4))))
print(result)
print(sum(result))
