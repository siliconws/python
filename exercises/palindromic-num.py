#Solution 1: Numeric Palindrome
def calculate(num: int) -> bool:

    new_num = 0
    original = num

    while num > 0:
        digit = num % 10
        new_num = (new_num * 10) + digit
        num //= 10

    return True if new_num == original else False



# Solution 2
def calculate_2(num: int) -> any:
    num = str(num)

    left = (len(num) - 1) // 2
    right = len(num) // 2

    while left >= 0 and right < len(num):
        if num[left] == num[right]:
            left -= 1
            right += 1
        else:
            return False

    return True


print(calculate_2(2882))


# Solution 3 - Reverse String
def calculate_3(num: int) -> bool:
    s = str(num)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
