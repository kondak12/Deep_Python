import threading
import time


def thread_counter(func):
    thread_count = 0
    def wrapper(*args, **kwargs):
        nonlocal thread_count
        thread_count += 1
        result = func(*args, **kwargs)
        print(f"thread count -> {thread_count}")
        return result
    return wrapper

@thread_counter
def new_thread(*args, **kwargs):
    threading.Thread(*args, **kwargs).start()

def thread_func(thread_count: int, sleep_time=0.0001):
    for i in range(thread_count):
        name = f"Поток {i}"
        new_thread(name=name)
        time.sleep(sleep_time)

thread_func(100)


# я эксперементировал и возможно сделал неправильно