# Task 1.1 -------------------------------------------------------------------------------------------------------------
def multiple_5_generator():
    num = 0
    while True:
        num += 5
        yield num

# Task 1.2 -------------------------------------------------------------------------------------------------------------
def num_square_generator():
    num = 1
    while True:
        yield num**2
        num += 1

# Task 1.3 -------------------------------------------------------------------------------------------------------------
def no_3_generator(end: int):
    current_num = 0
    while current_num != end+1:
        current_num += 1
        if not(current_num % 3 == 0):
            yield current_num

# Task 1.4 -------------------------------------------------------------------------------------------------------------
def string_split_generator(string: str, len_split: int):
    while len(string) != len_split-1:
        yield string[:len_split:]
        string = string[1:len(string)]

# Task 1.5 -------------------------------------------------------------------------------------------------------------
def diapason_plus_2_generator(first: int, last: int):
    while first <= last:
        yield first
        first += 2

# Task 1.6 -------------------------------------------------------------------------------------------------------------
import random

def infinity_random_generator():
    while True:
        yield random.randint(1, 100)

# Task 1.7 -------------------------------------------------------------------------------------------------------------
def fibonacci_generator():
    sequence = [0, 1]
    while True:
        yield sequence[0]
        sequence[0] = sequence[0] + sequence[1]
        yield sequence[1]
        sequence[1] = sequence[0] + sequence[1]