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
partial_sums, threads = [], []


def calculate_sum(current_split: int, start: int, end: int, index: int):
    current_sum = 0

    while start != end + 1:
        current_sum += split_list[current_split][start]
        start += 1

    if index > len(partial_sums) - 1:
        partial_sums.append(current_sum)
    elif index < len(partial_sums):
        partial_sums.insert(0, current_sum)
    else:
        partial_sums.insert(index, current_sum)


for i in range(5):
    name = f"Поток {i}"
    thread = threading.Thread(target=calculate_sum(i, 0, 4, i), name=name)
    thread.start()
    print(partial_sums) # "проверка" того, что список обновляется
    threads.append(thread)
    result = sum(partial_sums)

for t in threads:
    t.join()

print(result)