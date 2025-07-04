import threading
import time


def thread_target(name: str, sleep: int):
    print(f"Поток {name} начался")
    time.sleep(sleep)
    print(f"Поток {name} завершен")


def thread_logger(thread):

    def wrapper(*args, **kwargs):

        result = thread(*args, **kwargs)

        return result

    return wrapper


@thread_logger
def new_thread(th_name: str, sleep_time: int):
    return threading.Thread(target=thread_target(th_name, sleep_time), name=th_name)

new_thread("123", 2)