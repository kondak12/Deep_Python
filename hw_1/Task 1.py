"""
Задание 1:

Проблема:
    - Создайте декоратор `count_calls`, который подсчитывает, сколько раз была вызвана декорируемая функция, и выводит это число перед каждым вызовом.

Требования:
    - Счетчик должен быть связан с декорируемой функцией.
    - Декоратор должен работать с функциями, принимающими любые аргументы.
"""


def count_calls(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызвана {count} раз(а)")
        result = func(*args)
        return result
    return wrapper


@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
greet("Мария")