import threading
import time


def thread_func(th_name):
    print(f"Привет из потока '{th_name}'!")
    time.sleep(1)

threads = []

for i in range(1, 7):
    name = f"Поток {i}"
    thread = threading.Thread(target=thread_func(name), name=name)
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()