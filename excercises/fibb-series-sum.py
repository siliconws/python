
def calculate(a = 0, b = 1, num = 0):
    if not hasattr(calculate, 'fibb'):
        calculate.fibb = [a, b]

    if num < 900:
        if num % 2 == 0:
            a, b = b, a+b
            calculate.fibb.append(a)
        calculate(a, b, num + 1)

    return calculate.fibb

print(calculate())