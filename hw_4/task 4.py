import threading
import time


def thread_target(name: str, sleep: int):
    print(f"Поток {name} начался")
    time.sleep(sleep)
    print(f"Поток {name} завершен")


def new_thread(th_name: str, sleep_time: int):
    return threading.Thread(target=thread_target(th_name, sleep_time), name=th_name)

threads = [
    new_thread("123", 2),
    new_thread("234", 1),
    new_thread("345", 2)
]

for t in threads:
    t.start()

for t in threads:
    t.join()