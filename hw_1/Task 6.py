"""
Задание 6:

Проблема:
    - Создайте декоратор `call_limit`, который ограничивает количество вызовов функции. После достижения лимита при попытке вызова функции должно выдаваться исключение `RuntimeError`.

Требования
    - Декоратор должен принимать параметр `max_calls`, определяющий максимальное количество вызовов.
    - При превышении лимита должно генерироваться исключение с информативным сообщением.
    - Счетчик вызовов должен быть связан с декорируемой функцией.
"""


def call_limit(max_calls):

    def decorator(func):

        count_calls = 0

        def wrapper(*args, **kwargs):

            nonlocal count_calls
            count_calls += 1

            if count_calls > max_calls: raise RuntimeError(f"Превышено максимальное ({max_calls}) количество вызовов функции '{func.__name__}'")
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")    # Вывод: Первый вызов
print_message("Второй вызов")    # Вывод: Второй вызов
print_message("Третий вызов")    # Вывод: Третий вызов
print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '