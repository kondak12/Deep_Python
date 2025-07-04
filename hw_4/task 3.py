import threading
import time


def thread_counter(func):

    thread_count = 0

    def wrapper(*args, **kwargs):
        nonlocal thread_count

        thread_count += 1
        print(f"thread count -> {thread_count}")

        return func(*args, **kwargs)

    return wrapper


@thread_counter
def new_thread(*args, **kwargs):
    return threading.Thread(*args, **kwargs)


def thread_func(thread_count: int, sleep_time=0.0001):

    threads = []

    for i in range(thread_count):
        name = f"Поток {i}"
        thread = new_thread(name=name)
        thread.start()
        threads.append(thread)
        time.sleep(sleep_time)

    for t in threads:
        t.join()

thread_func(100)