import threading
import random


shared_list = []
list_lock = threading.Lock()

def add_random_numbers():
    with list_lock:
        [shared_list.append(random.randint(1, 333)) for _ in range(5)]


threads = []

for i in range(1, 4):
    name = f"Поток {i}"
    thread = threading.Thread(target=add_random_numbers(), name=name)
    thread.start()
    print(shared_list) # "проверка" того, что список обновляется
    threads.append(thread)

for t in threads:
    t.join()