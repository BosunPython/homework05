"""Написать программу, которая будет создавать класс данных из JSON объекта.
(Дополнительно): Добавить метод для данного класса,
который будет выводить все поля класса. """

import json

class Transport:
    def __init__(self, dict):
        vars(self).update(dict)

dict1 = '{"Technics": {"Auto": "wheel","Tractor":["caterpillar", "wheel"]}}'

New_transport = json.loads(dict1, object_hook= Transport)

print(New_transport.Technics.Tractor[0])

