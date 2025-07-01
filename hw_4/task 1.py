import random
import threading
import time


def thread_func(th_name):
    print(f"Привет из потока '{th_name}'!")
    time.sleep(random.randint(1, 3))


for i in range(random.randint(5, 8)):
    name = f"Поток {i}"
    thread = threading.Thread(target=thread_func(name), name=name)
    thread.start()