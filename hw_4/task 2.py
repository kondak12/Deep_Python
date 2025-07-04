import threading
import random
import time


class MyThread(threading.Thread):

    name: str
    sleep_time: int

    def __init__(self, name: str, sleep_time: int):

        super().__init__()

        if sleep_time < 0: raise ValueError("Время сна не может быть отрицательным.")

        self.__name = name
        self.__sleep_time = sleep_time

    def run(self):
        print(f"Поток {self.__name} работает")
        time.sleep(self.__sleep_time)
        print(f"Поток {self.__name} закончил работу")


mt = MyThread("Name!", 3)

for i in range(random.randint(5, 10)):
    mt.run()