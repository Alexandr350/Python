import sys

class Transport(object):
    capacity = 5
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def obj_print(self):
        print(f'Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}')

    def seating_capacity(self):
        return f"Вместимость {self.name}  {self.capacity} пассажиров"

class Autobus(Transport):
    capacity = 50
    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}  {self.capacity} пассажиров"


avto = Transport('Renaul Logan', 180, 12)
avtobus = Autobus('Renaul Logan', 180, 12)
avto.obj_print()
print(avto.seating_capacity())
print(avtobus.seating_capacity())
avtobus.capacity = 70
print(avtobus.seating_capacity())
print(sys.stdin.readline())