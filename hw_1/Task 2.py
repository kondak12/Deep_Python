"""
Задание 2:

Проблема:
    - Создайте декоратор `type_check`, который проверяет типы аргументов декорируемой функции. Декоратор должен принимать ожидаемые типы аргументов в виде кортежа.

Требования:
    - Если типы аргументов не соответствуют ожидаемым, выбрасывается `TypeError` с сообщением об ошибке.
    - Декоратор должен работать с функциями с любым количеством аргументов.
"""


def type_check(*types):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(f"Неверный тип аргумента '{func.__code__.co_varnames[i]}'. Ожидался {types[i]}, получен {type(args[i])}")
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


print(add(2, 3))     # 5
print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>