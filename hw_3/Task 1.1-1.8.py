import re

# Task 1.1 -------------------------------------------------------------------------------------------------------------
def invert_range(a: int, b: int):
    if a < b: raise ValueError("a < b")
    while a != b-1:
        yield a
        a -= 1

# Task 1.2 -------------------------------------------------------------------------------------------------------------
def multiple_5_fibonacci():
    sequence = [0, 1]
    while True:

        if sequence[0] % 5 == 0:
            yield sequence[0]

        sequence[0] = sequence[0] + sequence[1]

        if sequence[1] % 5 == 0:
            yield sequence[1]

        sequence[1] = sequence[0] + sequence[1]

# Task 1.3 -------------------------------------------------------------------------------------------------------------
from functools import reduce

def factorial_generator():
    number = 1
    while True:
        yield reduce(lambda a, b: a * b, [_ for _ in range(1, number+1)])
        number += 1

# Task 1.4 -------------------------------------------------------------------------------------------------------------
def alphabet_generator():
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    while True:
        for sym in range(len(alphabet)):
            yield alphabet[sym]

# Task 1.5 -------------------------------------------------------------------------------------------------------------
def unic_string_words(string: str):
    string = [set(re.split(" |, |. ", string))]
    for word in string:
        yield word

# Task 1.6 -------------------------------------------------------------------------------------------------------------
def word_len_sorter(string: str, min_word_len: int):
    string = string.split(" ")
    for word in string:
        if len(word) >= min_word_len:
            yield word

# Task 1.7 -------------------------------------------------------------------------------------------------------------
from itertools import permutations

def all_sequences(string: str, max_len: int):
    for i in range(1, max_len + 1):
        for p in permutations(string, i):
            yield "".join(p)

# Task 1.8 -------------------------------------------------------------------------------------------------------------
def unic_vowel_letter(string: str):
    vowel = ["a", "e", "i", "o", "u", "y"]
    for letter in set(list(string.lower())):
        if letter in vowel:
            yield letter