def calculate():

    max_palindrome = 0

    for i in range(10, 100):
        for j in range(10, 100):

            product = i * j

            # reverse the number
            temp = product
            reverse_num = 0

            while temp > 0:
                reverse_num = reverse_num * 10 + temp % 10
                temp //= 10

            if product == reverse_num and product > max_palindrome:
                max_palindrome = product

    return max_palindrome
    
    
print(calculate())


# Solution 2
def calculate_2():
    numbers = []
    for i in range(10, 100):
        for j in range(10, 100):
            if str(i * j) == str(i * j)[::-1]:
                numbers.append(i * j)
    return max(numbers)
 
 
print(calculate_2())


# Solution 3
def calculate_3():
    result = max([i * j
                  for i in range(10, 100)
                  for j in range(10, 100)
                  if str(i * j) == str(i * j)[::-1]])
    return result
 

print(calculate_3())