from typing import Iterator

def prime_factorization(num: int = 1) -> Iterator[int]:

    if num < 2:
        yield 2

    for prime in range(2, num+1):
        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            yield prime


def calculate(num: int = 10):
    # Create a list to store the prime factors
    factors = []

    # Create an Iterator object 
    a = prime_factorization(num)

    for prime in a:
        while num % prime == 0:
            factors.append(prime)
            num //= prime

            if num < 2:
                break

    return factors


print(calculate(15))