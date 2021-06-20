"""
Основы Python
ДЗ 7 Гладышев ВВ
"""

from abc import ABC, abstractmethod

"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), 
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    """
    класс - Матрица

    методы:
    __init__
    __str__
    __add__
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __add__(self, other):
        pass


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    pass

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) 
этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes(ABC):
    """
    абстрактный класс - Одежда
    """
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    """
    класс - Пальто
    """
    def fabric_consumption(self):
        pass


class Suit(Clothes):
    """
    класс - Костюм
    """
    def fabric_consumption(self):
        pass


answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    pass

r"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), 
умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, 
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() 
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() 
вернет строку: *****\n*****\n*****.
"""


class Cell:
    """
    класс - Клетка
    """
    pass


answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    pass
