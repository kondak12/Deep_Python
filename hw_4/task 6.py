import threading
import random


int_list = [random.randint(1, 333) for _ in range(100)]

def list_splitter(list: list):

    result = []

    for i in range(len(list) // 20):
        part = []
        for j in range(len(list) // 5):
            part.append(list[j])
            list.pop(j)
        result.append(part)

    return result


split_list = list_splitter(int_list)
lists_sum, threads = [], []

for i in range(5):
    name = f"Поток {i}"
    thread = threading.Thread(target=lists_sum.append(sum(split_list[i])), name=name)
    thread.start()
    print(lists_sum) # "проверка" того, что список обновляется
    threads.append(thread)
    result = sum(lists_sum)

for t in threads:
    t.join()

print(result)