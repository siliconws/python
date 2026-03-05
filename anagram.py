# First approach
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    dict1 = {}
    for char in str1:
            dict1[char] = dict1.get(char, 0) + 1

    for char in str2:
        if dict1.get(char, 0) == 0:
            return False
        dict1[char] -= 1

    return True


print(is_anagram("evil", "lveli"))

# Second approach
def is_anagram_2(str1, str2):
    if len(str1) != len(str2):
        return False

    count_chars = {}
    for char in str1:
        count_chars[str1[char]] = count_chars.get(char, 0) + 1
        count_chars[str2[char]] = count_chars.get(char, 0) - 1

    return all(value == 0 for value in count_chars.values())


print(is_anagram_2("evil", "lveli"))