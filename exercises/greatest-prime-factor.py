from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")

def calculate(n):

    factors = []

    while n % 2 == 0:
        n //= 2
        factors.append(2)

    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 2

    if n > 1:
        factors.append(n)

    return max(factors)


with timer():
    print(calculate(13195))