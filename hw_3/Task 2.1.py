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


class SecuritySystem:

    def requires_access(self, zone):
        pass

    def enter_zone(self, employee, zone):
        pass