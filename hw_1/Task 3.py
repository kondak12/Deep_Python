"""
Задание 3:

Проблема:
    - Создайте декоратор `validate_range`, который проверяет, что все числовые аргументы функции находятся в заданном диапазоне. Если какой-либо аргумент выходит за пределы диапазона, следует вызвать `ValueError`.

Требования:
    - Декоратор должен принимать два параметра: `min_value` и `max_value`.
    - Проверять нужно все аргументы типа `int` или `float`.
    - В сообщении об ошибке укажите имя аргумента и его значение.
"""


def validate_range(min_value, max_value):

    def decorator(func):

        def wrapper(value):

            if not isinstance(value, int or float): raise TypeError(f"Неверный тип аргумента. Ожидался <class 'int'> или <class 'float'>, получен {type(value)}")

            if not (min_value <= value <= max_value): raise ValueError(f"Аргумент '{func.__code__.co_varnames[0]}' имеет значение {value}, что выходит за пределы [{min_value}, {max_value}]")

            result = func(value)

            return result

        return wrapper

    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")

set_percentage(70)
set_percentage(101)