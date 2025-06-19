"""
Задание 5:

Проблема:
    - Создайте декоратор `uppercase_result`, который преобразует строковый результат функции в верхний регистр перед его возвращением.

Требования:
    - Декоратор должен проверять, что результат функции является строкой.
    - Если результат не строка, возвращать его без изменений.
    - Декоратор должен работать с функциями, возвращающими различные типы данных.
"""


def uppercase_result(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if isinstance(result, str): result = result.upper()

        return result

    return wrapper


@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ

@uppercase_result
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 123))  # Вывод: 5