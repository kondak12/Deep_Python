"""
Задание 4:

Проблема:
    - Создайте декоратор `trace`, который выводит информацию о вложенности вызовов функций (стек вызовов). При каждом входе и выходе из функции должно выводиться сообщение с указанием имени функции и уровня вложенности.

Требования:
    - Уровень вложенности должен отображаться с помощью отступов.
    - Декоратор должен корректно работать с рекурсивными функциями.
"""


def trace(func):

    count = -1

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        print(f"{"\t"*count}--> Вход в функцию '{func.__name__}' с аргументами {args}, {kwargs}")
        result = func(*args)

        print(f"{"\t"*count}<-- Выход из функции '{func.__name__}' с результатом {result}")
        count -= 1

        return result

    return wrapper


@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)