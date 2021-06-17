"""
Основы Python
ДЗ 5 Гладышев ВВ
"""

import time

"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, 
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном 
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее 
сообщение и завершать скрипт.
"""


class TrafficLight:
    """
    класс Светофор
    """

    _color: int
    _color_list: list = ["красный", "желтый", "зеленый"]
    _color_time_list: list = [7, 2, 7]

    def __init__(self) -> None:
        self._color = 0

    def running(self):
        for _ in range(3):
            print(f"\r\t{self._color_list[self._color]}", end='')
            time.sleep(self._color_time_list[self._color])
            self._color = 0 if self._color == 2 else self._color + 1
        print("\n")


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    trafficLight = TrafficLight()
    trafficLight.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    """
    класс для расчёта массы асфальта
    """

    _length: float
    _width: float
    _thickness: float = 5   # толщина по умолчанию 5 см
    _mass_per_centimeter = 25   # масса (кг) асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см

    def __init__(self, length: float, width: float) -> None:
        self._length = length
        self._width = width

    def print_asphalt_weight(self):
        """
        расчёт и печать массы асфальта для дороги

        формула длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
        толщиной в 1 см*число см толщины полотна
        """
        print(f"\tМасса асфальта: {self._length*self._width*self._thickness*self._mass_per_centimeter/1000:.2f} т.")


answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    try:
        r_length = abs(float(input("\n\tВведите длину дороги (в метрах): ")))
        r_width = abs(float(input("\tВведите ширину дороги (в метрах): ")))
    except ValueError:
        print(f"Ошибка приведения аргумента к float!")
    else:
        road = Road(r_length, r_width)
        road.print_asphalt_weight()
        print()

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом 
премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """
    класс Работник
    """

    _name: str
    _surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super()
        self._name = name
        self._surname = surname
        self.position = position
        try:
            wage = float(wage)
            bonus = float(bonus)
        except ValueError:
            print(f"Ошибка приведения аргумента к float!")
        else:
            self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """
    класс Должность
    """

    def get_full_name(self) -> str:
        """
        Формирует строку с полным именем: Фамилия Имя
        """
        return self._surname + " " + self._name

    def get_total_income(self) -> float:
        """
        Формирует сумму полного дохода: wage + bonus
        """
        return self._income["wage"] + self._income["bonus"]


answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    pos_programmer = Position("Иван", "Иванов", "Программист", 70000, 30000)
    pos_economist = Position("Пётр", "Петров", "Экономист", 60000, 30000)
    pos_lawyer = Position("Семён", "Сидоров", "Юрист", 60000, 50000)

    print(f"\t{pos_programmer.position} {pos_programmer.get_full_name()} зарплата: {pos_programmer.get_total_income()}")
    print(f"\t{pos_economist.position} {pos_economist.get_full_name()} зарплата: {pos_economist.get_total_income()}")
    print(f"\t{pos_lawyer.position} {pos_lawyer.get_full_name()} зарплата: {pos_lawyer.get_total_income()}\n")

"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

answer = input("Задание 4 (д/н)? ")
if answer == 'д':
    pass

"""
5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""

answer = input("Задание 5 (д/н)? ")
if answer == 'д':
    pass

"""
6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и 
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет 
описанный метод для каждого экземпляра.
"""

answer = input("Задание 6 (д/н)? ")
if answer == 'д':
    pass
