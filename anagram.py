
def is_anagram(a: str, b: str) -> bool:
    """ Check if two strings are anagrams using frequency counting. """

    if len(a) != len(b):
        return False

    count_chars = {}
    for char in a:
            count_chars[char] = count_chars.get(char, 0) + 1

    for char in b:
        if count_chars.get(char, 0) == 0:
            return False
        count_chars[char] -= 1

    return True


print(is_anagram("listen","silent"))
print(is_anagram("triangle","integral"))
print(is_anagram("evil","vill"))
print(is_anagram("evil","lveli"))


def is_anagram_2(a: str, b: str) -> bool:
    """ Check anagram using single pass balancing. """

    if len(a) != len(b):
        return False

    count_chars = {}
    for a_char, b_char in zip(a, b):
        count_chars[a_char] = count_chars.get(a_char, 0) + 1
        count_chars[b_char] = count_chars.get(b_char, 0) - 1

    return all(value == 0 for value in count_chars.values())


print(is_anagram_2("listen","silent"))
print(is_anagram_2("triangle","integral"))
print(is_anagram_2("evil","vill"))
print(is_anagram_2("evil","lveli"))