"""
Основы Python
ДЗ 7 Гладышев ВВ
"""

from typing import List
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
    matrix: List[List[float]]

    def __init__(self, matrix: List[List[float]]) -> None:
        """
        Конструктор
        :param matrix:
        """
        self.matrix = matrix
        try:
            for raw_ind in range(len(self.matrix)):
                for el_ind in range(len(self.matrix[0])):
                    self.matrix[raw_ind][el_ind] = float(self.matrix[raw_ind][el_ind])
        except (ValueError, IndexError) as error:
            print(f"\nОшибка при создании объекта: {error}!\n")
            self.matrix = []
            return

    def __str__(self) -> str:
        """
        Распечатываем матрицу
        :return: строка с матрицей
        """
        res_str: str = ""
        try:
            for raw in self.matrix:
                res_str += "\t"
                for el in raw:
                    res_str += f"{el} "
                res_str += "\n"
        except ValueError as error:
            return f"\nОшибка: {error}!\n"
        return res_str

    def __add__(self, other):
        """
        Сложение матриц
        :param other: второе слагаемое
        :return: self or None
        """
        if len(self.matrix) != len(other.matrix):
            print("В матрицах разное количество строк!")
            return
        if len(self.matrix[0]) != len(other.matrix[0]):
            print("В матрицах разное количество столбцов!")
            return
        try:
            for raw_ind in range(len(self.matrix)):
                for el_ind in range(len(self.matrix[0])):
                    self.matrix[raw_ind][el_ind] += float(other.matrix[raw_ind][el_ind])
        except IndexError as error:
            print(f"\nОшибка при сложении: {error}!\n")
            self.matrix = []
            return
        else:
            return self


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

    matrix_obj_a = Matrix(matrix_a)
    matrix_obj_b = Matrix(matrix_b)

    print("\tПервая матрица:")
    print(f"\tСписок списков\n\t{matrix_a}\n")
    print(f"\tОбъект класса\n{matrix_obj_a}")
    print("\tВторая матрица:")
    print(f"\tСписок списков\n\t{matrix_b}\n")
    print(f"\tОбъект класса\n{matrix_obj_b}")
    print(f"\tСумма матриц:\n{matrix_obj_a + matrix_obj_b}")

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

    size: float   # размер пальто

    def __init__(self, size: float):
        """
        Конструктор класса Coat

        :param size: размер пальто
        """
        try:
            self.size = float(size)
        except ValueError:
            print(f"\nОшибка при приведении параметра к float. Установлен размер по умолчанию: 50\n")
            self.size = 50.

    @property
    def fabric_consumption(self):
        """
        Реализация абстрактного метода
        Расчёт расхода ткани для пальто
        Формула расхода ткани для пальто: size/6.5 + 0.5

        :return: количество ткани
        """
        return self.size/6.5 + 0.5


class Suit(Clothes):
    """
    класс - Костюм
    """

    height: float  # рост

    def __init__(self, height: float):
        """
        Конструктор класса Suit

        :param height: рост
        """
        try:
            self.height = float(height)
        except ValueError:
            print(f"\nОшибка при приведении параметра к float. Установлен рост по умолчанию: 170\n")
            self.height = 170.

    @property
    def fabric_consumption(self):
        """
        Реализация абстрактного метода
        Расчёт расхода ткани для костюма
        Формула расхода ткани для костюма: 2 * height + 0.3

        :return: количество ткани
        """
        return 2 * self.height + 0.3


answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    coat = Coat(48)
    suite = Suit(170)

    print(f"\tРазмер пальто: {coat.size} Расход ткани: {coat.fabric_consumption:.2f}")
    print(f"\tРазмер костюма: {suite.height} Расход ткани: {suite.fabric_consumption:.2f}\n")

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

    _cell_number: int   # количество ячеек

    def __init__(self, cell_number):
        """
        Конструктор класса Cell

        :param cell_number: начальное число ячеек
        """
        self._cell_number = cell_number

    def get_cell_number(self):
        """
        Возвращает защищённый параметр _cell_number

        :return: _cell_number
        """
        return self._cell_number

    def __add__(self, other):
        """
        Сложение числа ячеек двух объектов Cell

        :param other: слагаемое - другой объект Cell
        :return: объект класса Cell с числом ячеек равным сумме
        """
        return Cell(self._cell_number + other.get_cell_number())

    def __sub__(self, other):
        """
        Разность числа ячеек двух объектов Cell

        :param other: вычитаемое - другой объект Cell
        :return: объект класса Cell с числом ячеек равным разности
        """
        difference = self._cell_number - other.get_cell_number()
        if difference >= 0:
            return Cell(difference)
        else:
            print("Разность меньше нуля!")
            return Cell(0)

    def __mul__(self, other):
        """
        Произведение числа ячеек двух объектов Cell

        :param other: множитель - другой объект Cell
        :return: объект класса Cell с числом ячеек равным произведению
        """
        product = self._cell_number * other.get_cell_number()
        if product >= 0:
            return Cell(product)
        else:
            return Cell(0)

    def __truediv__(self, other):
        """
        Частное целочисленного деления ячеек двух объектов Cell

        :param other: делитель - другой объект Cell
        :return: объект класса Cell с числом ячеек равным частному целочисленного деления
        """
        if int(other.get_cell_number()) != 0:
            return Cell(self._cell_number // other.get_cell_number())
        else:
            print("Попытка деления на ноль!")
            return self

    def __str__(self):
        """
        Вывод 'организма' из ячеек фиксированно по 5 в ряд
        :return: сформированная строка
        """
        return self.make_order(5)

    def make_order(self, line_width):
        """
        Форматированный вывод 'организма' из ячеек

        :param line_width: количество ячеек в строке
        :return: сформированная строка
        """
        whole: int = self._cell_number // line_width
        remainder: int = self._cell_number % line_width
        res_str: str = f"\tЯчеек: {self._cell_number}\n"
        if not (whole or remainder):
            return "\tНет ячеек :(\n"
        if whole:
            res_str += (("\t"+"*"*line_width+"\n")*whole)
        if remainder:
            res_str += ("\t"+"*"*remainder+"\n")
        return res_str


answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    org_1 = Cell(6)
    org_2 = Cell(12)
    org_3 = Cell(24)

    print("\tОрганизм 1:")
    print(f"{org_1}")
    print("\tОрганизм 2:")
    print(f"{org_2}")
    print("\tОрганизм 3:")
    print(f"{org_3.make_order(6)}")
    print("\tСумма первого и второго:")
    print(org_1+org_2)
    print("\tРазность третьего и второго:")
    print(org_3-org_2)
    print("\tПроизведение первого и второго:")
    print(org_1*org_2)
    print("\tЦелочисленное частное третьего и первого:")
    print(org_3/org_1)
