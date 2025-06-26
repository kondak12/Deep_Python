import datetime


zones = {
    "COFFEE": "Coffee",
    "STORAGE": "Storage",
    "LAB": "Lab",
    "LOBBY": "Lobby"
}


class Employee:

    name: str
    access_zones: list

    def __init__(self, name: str, access_zones: list):

        for i in range(len(access_zones)):
            if access_zones[i] not in zones:
                raise ValueError("Переданной зоны в зонах доступа не существует")

        self.__name = name
        self.__access_zones = set(access_zones)

    def get_name(self):
        return self.__name

    def get_access_zones(self):
        return self.__access_zones


def requires_access(func):

    def wrapper(self, *args, **kwargs):

        if args:
            employee, zone = args
        elif kwargs:
            employee, zone = kwargs.values()

        if zone not in employee.get_access_zones():
            print("Доступ запрещён.")
            self.access_code = 0

        else:
            result = func(*args, **kwargs)
            self.access_code = 1

            return result

    return wrapper


def log_access(func):

    def wrapper(self, *args, **kwargs):

        if args:
            employee, zone = args
        elif kwargs:
            employee, zone = kwargs.values()

        if self.access_code == 1:
            self.__access_denied.append(f"{employee.get_name()} ({datetime.datetime})")
        else:
            result = func(*args, **kwargs)
            self.__access_granted.append(f"{employee.get_name()} ({datetime.datetime})")

            return result

    return wrapper


class SecuritySystem:

    def __init__(self):
        self.access_granted = []
        self.access_denied = []
        self.access_code = None

    @log_access
    @requires_access
    def enter_zone(self, employee: Employee, zone: str):
        print(f"Доступ разрешён, добро пожаловать {employee.get_name()}!")


e1 = Employee("Lan", ["COFFEE", "STORAGE"])
e2 = Employee("Voa", ["STORAGE", "LAB"])

ss = SecuritySystem()


# Я старался, не вышло. До конца не понятно как это делается.