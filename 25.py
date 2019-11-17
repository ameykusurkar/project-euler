def fib():
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x + y

def first_match(iterable, condition):
    return next(x for x in iterable if condition(x))

print(first_match(enumerate(fib(), 1), lambda f: len(str(f[1])) == 1000))
