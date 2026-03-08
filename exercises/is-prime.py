# Solution 1
import math

def is_prime(num: int) -> bool:

    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


print(is_prime(1))


# Solution 2
def is_prime_2(num: int = 1) -> bool:

    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True


print(is_prime_2(1))


# Solution 3
def is_prime_3(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


print(is_prime_3(1))
