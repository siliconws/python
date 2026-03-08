def is_prime(n):

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

def calculate():

    count = 1
    num = 1

    while count < 100:
        num += 2

        if is_prime(num):
            count += 1

    return num

print(calculate())