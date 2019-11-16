def fib():
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x + y

fibs = fib()

for i, f in enumerate(fibs, 1):
    if len(str(f)) == 1000:
        print(i, f)
        break
