import re


def count_vowels(str):
    return len(re.findall(r'[aeiou]', str, re.IGNORECASE))


count_vowels("Python")