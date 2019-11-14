from itertools import takewhile

def fib():
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x + y

fibs = fib()
next(fibs) # We want to start 1, 2, ...

small_fibs = takewhile(lambda x: x <= 4_000_000, fibs)
even_fibs = filter(lambda x: x % 2 == 0, small_fibs)

print(sum(even_fibs))
