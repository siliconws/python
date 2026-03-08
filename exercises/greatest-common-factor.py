def greatest_common_divisor(small, big):
    while big > 0:
        small, big = big, small % big

    return small

print(greatest_common_divisor(32, 48))