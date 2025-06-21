from functools import reduce

# Task 1 ---------------------------------------------------------------------------------------------------------------
print("Task 1")

for _ in map(lambda string: int(string), ["1", "20", "300"]):
    print(_)

# Task 2 ---------------------------------------------------------------------------------------------------------------
print("\nTask 2")

for _ in filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6]):
    print(_)

# Task 3 ---------------------------------------------------------------------------------------------------------------
print("\nTask 3")

for _ in map(lambda num: num**2, [1, 2, 3, 4]):
    print(_)

# Task 4 ---------------------------------------------------------------------------------------------------------------
print("\nTask 4")

for _ in filter(lambda elem: len(elem) > 3 and isinstance(elem, str), ["cat", "elephant", "dog", "tiger"]):
    print(_)

# Task 5 ---------------------------------------------------------------------------------------------------------------
print("\nTask 5")

print(reduce(lambda elem1, elem2: elem1 * elem2, [1, 2, 3, 4]))

# Task 6 ---------------------------------------------------------------------------------------------------------------
print("\nTask 6")

for _ in map(lambda elem: len(elem), ["hello", "world", "Python"]):
    print(_)

# Task 7 ---------------------------------------------------------------------------------------------------------------
print("\nTask 7")

print(max(map(lambda elem: len(elem), ["apple", "banana", "pear", "strawberry"])))

# Task 8 ---------------------------------------------------------------------------------------------------------------
print("\nTask 8")

for _ in map(lambda elem: elem.upper(), ["hello", "world"]):
    print(_)

# Task 9 ---------------------------------------------------------------------------------------------------------------
print("\nTask 9")

for _ in filter(lambda elem: elem % 2 == 0, (map(lambda elem: int(elem)**2, ["1", "2", "3", "4"]))):
    print(_)

# Task 10 --------------------------------------------------------------------------------------------------------------
print("\nTask 10")

print(reduce(lambda elem1, elem2: elem1 * elem2, filter(lambda elem: elem > -1, [-2, 3, -4, 5, 6])))

# Task 11 --------------------------------------------------------------------------------------------------------------
print("\nTask 11")

for _ in map(lambda elem: len(elem), filter(lambda elem: elem[0] in ["a", "e", "i", "o", "u", "y"], ["apple", "banana", "orange", "grape"])):
    print(_)

# Task 12 --------------------------------------------------------------------------------------------------------------
print("\nTask 12") # ?

for _ in filter(lambda elem: elem == elem.reverse(), map(lambda string: [sym for sym in string], ["racecar", "hello", "level", "world"])):
    print(_)

# Task 13 --------------------------------------------------------------------------------------------------------------
print("\nTask 13")

print(reduce(lambda elem1, elem2: elem1 * elem2, map(lambda elem: reduce(lambda elem1, elem2: elem1 * elem2, [num for num in range(1, elem+1)]), filter(lambda elem: elem % 2 == 0, [2, 3, 4, 5, 6]))))
print("В условии неверный ответ.")

# Task 14 --------------------------------------------------------------------------------------------------------------
print("\nTask 14")

print(reduce(lambda word1, word2: word1 + " " + word2, map(lambda word: word.upper(), filter(lambda string: len(string) % 2 == 0, ["hello", "world", "Python", "is", "great"]))))
print("В условии неверный ответ.")