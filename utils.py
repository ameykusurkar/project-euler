import time

def timeit(f):
    def decorated(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print(f"{time.time() - start} seconds")
        return result
    return decorated
