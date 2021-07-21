"""
Основы Python
ДЗ 8 Гладышев ВВ
"""

"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """
    Класс Дата
    содержит методы:
        parse_date() для выделения года, месяца и дня
        check_date() для валидации числа, месяца и года
    """

    @classmethod
    def parse_date(cls, inc_date: str) -> tuple:
        """
        Выделение года, месяца и дня из строки
        :param inc_date: str: строка с датой
        :return: tuple:  year, month, day
        """
        year: int = -1   # год
        month: int = -1  # месяц
        day: int = -1    # день

        separators_list: list = [' ', '.', '/', '-', '_', '\\']
        split_list: list = [inc_date]

        for sp in separators_list:
            internal_list: list = []
            for el in split_list:
                internal_list.extend(el.split(sp))
            split_list = internal_list

        numbers_list: list = []
        for el in split_list:
            if str(el).isdecimal() and len(el) < 5:
                numbers_list.append(int(el))

        len_four: int = 0
        for ind in reversed(range(len(numbers_list))):
            if len(str(numbers_list[ind])) == 4:
                len_four = ind

        if len(numbers_list) > 2:
            if len_four:
                day = numbers_list[0]
                month = numbers_list[1]
                year = numbers_list[2]
            else:
                year = numbers_list[0]
                month = numbers_list[1]
                day = numbers_list[2]

        return year, month, day

    @staticmethod
    def check_date(check_str: str) -> bool:
        """
        проверка числа, месяца и года
        :param check_str: str: строка с датой
        :return: bool: флаг: True - корректна, False - некорректна
        """
        date_corr: bool = True
        year, month, day = Date.parse_date(check_str)
        if not 0 <= year <= 3000:
            date_corr = False
        if not 1 <= month <= 12:
            date_corr = False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not 1 <= day <= 31:
                date_corr = False
        elif month in [4, 6, 9, 11]:
            if not 1 <= day <= 30:
                date_corr = False
        elif month == 2:
            if not 1 <= day <= 29:
                date_corr = False
        return date_corr


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    my_date = Date()
    date_1 = " бла бла _2020/12\\3"
    print(f"\t{my_date.parse_date(date_1)}")
    if my_date.check_date(date_1):
        print("\t\tДата корректна")
    else:
        print("\t\tДата некорректна")

    date_2 = "чих пых _1221_06_15"
    print(f"\t{my_date.parse_date(date_2)}")
    if my_date.check_date(date_2):
        print("\t\tДата корректна")
    else:
        print("\t\tДата некорректна")

    date_3 = "тыр 30/2/1689 пыр"
    print(f"\t{my_date.parse_date(date_3)}")
    if my_date.check_date(date_3):
        print("\t\tДата корректна")
    else:
        print("\t\tДата некорректна")
    print()

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой.
"""


class ExceptionZeroDiv(ZeroDivisionError):
    """
    Класс исключение. Обрабатывает деление на 0
    """
    f_divisible: float   # делимое
    f_divisor: float     # делитель

    def __init__(self, f_divisible: float, f_divisor: float) -> None:
        self.f_divisible = f_divisible
        self.f_divisor = f_divisor

    def __str__(self):
        return f"\tДелимиое {self.f_divisible} делитель {self.f_divisor}. Делить на ноль не следует!"


class MyFloat(float):
    """
    Класс float с перегрузкой операций деления
    """
    my_float: float

    def __init__(self, inc_float: float) -> None:
        self.my_float = float(inc_float)

    def __truediv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float / other)

    def __floordiv__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float // other)

    def __mod__(self, other):
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return MyFloat(self.my_float % other)

    def __divmod__(self, other) -> tuple:
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            return divmod(self.my_float, other)

    # def __rtruediv__(self, other):
    # def __rfloordiv__(self, other):
    # def __rmod__(self, other):
    # def __rdivmod__(self, other):

    def __itruediv__(self, other):   # /=
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float /= other
            return MyFloat(self.my_float)

    def __ifloordiv__(self, other):   # //=
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float //= other
            return MyFloat(self.my_float)

    def __imod__(self, other):    # %=
        if other == 0:
            raise ExceptionZeroDiv(self.my_float, other)
        else:
            self.my_float %= other
            return MyFloat(self.my_float)


answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    a = MyFloat(10)
    b = MyFloat(2)
    c = MyFloat(0)

    a /= b
    # print(f"\t{divmod(a, 0)}")
    # a += b
    print(f"\t{a}")
    try:
        print(f"\t{a/b}")
        print(f"\t{a/0}")
        print(f"\t{a/c}")
        print(f"\t{c/0}")
        print(f"\t{c/a}")
    except ExceptionZeroDiv as error:
        print(error)
    print()

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только
числами. Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExceptionListOfNumbers(Exception):
    """
    Класс исключение. Вызывается если введённое значение не является целым числом
    """
    st_not_number: str   # нечисловое значение

    def __init__(self, st_not_number: str) -> None:
        self.st_not_number = str(st_not_number)

    def __str__(self):
        return f"\tЗначение {self.st_not_number} не является целым числом! Будет проигнорировано"


class NumbersList(list):
    """
    Класс список. Допустимы только числовые значения
    """
    def __init__(self, income_list: list):
        filtered_inc_list = []
        for el in income_list:
            if str(el).isdecimal():
                filtered_inc_list.append(int(el))
            else:
                try:
                    raise ExceptionListOfNumbers(str(el))
                except ExceptionListOfNumbers as err:
                    print(err)

        super(NumbersList, self).__init__(filtered_inc_list)

    def append(self, __object) -> None:
        if str(__object).isnumeric():
            super().append(int(__object))
        else:
            raise ExceptionListOfNumbers(str(__object))

    def extend(self, __iterable) -> None:
        for el in __iterable:
            if str(el).isdecimal():
                super().append(int(el))
            else:
                raise ExceptionListOfNumbers(str(el))


answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    my_list = NumbersList([12, 34, "кхм", 5656, 345.45])
    # my_list.extend([12, 34, 5656])
    while True:
        try:
            input_value = input("\tВведите целое число: ")
            if input_value == 'стоп':
                break
            my_list.append(input_value)
        except ExceptionListOfNumbers as error:
            print(error)

    print(f"\t{my_list}\n")

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEqStorage:
    """Класс - Склад оргтехники"""
    pass


class OfficeEquipment:
    """Базовый класс для офисной техники"""
    name: str   # Название

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"\t{self.name}\n"


class Printer(OfficeEquipment):
    """Класс Принтер"""
    __print_counter: int   # счётчик распечатанных страниц

    def __init__(self, name: str):
        super(Printer, self).__init__(name)
        self.__print_counter = 0

    def __str__(self):
        return super(Printer, self).__str__() + f"\t\tСчётчик печати: {self.__print_counter}\n"

    def make_print(self):
        self.__print_counter += 1

    def get_print_counter(self):
        return self.__print_counter


class Scanner(OfficeEquipment):
    """Класс сканер"""
    __scan_counter: int  # счётчик распечатанных страниц

    def __init__(self, name: str):
        super(Scanner, self).__init__(name)
        self.__scan_counter = 0

    def __str__(self):
        return super(Scanner, self).__str__() + f"\t\tСчётчик сканирования: {self.__scan_counter}\n"

    def make_scan(self):
        self.__scan_counter += 1

    def get_scan_counter(self):
        return self.__scan_counter


class Copier(OfficeEquipment):
    """Класс копир"""
    __copy_counter: int   # счётчик распечатанных страниц

    def __init__(self, name: str):
        super(Copier, self).__init__(name)
        self.__copy_counter = 0

    def __str__(self):
        return super(Copier, self).__str__() + f"\t\tСчётчик копирования: {self.__copy_counter}\n"

    def make_copy(self):
        self.__copy_counter += 1

    def get_copy_counter(self):
        return self.__copy_counter


answer = input("Задание 4, 5, 6 (д/н)? ")
if answer == 'д':
    printer_1 = Printer("HP 1536")
    print(printer_1)
    scanner_1 = Scanner("Epson 310")
    print(scanner_1)
    copier_1 = Copier("Xerox 1000")
    print(copier_1)
    # print()

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    """Класс Комплексное число"""
    i_real: int    # действительная часть
    i_imaginary: int    # мнимая часть

    def __init__(self, i_real: int, i_imaginary: int):
        self.i_real = i_real
        self.i_imaginary = i_imaginary

    def __add__(self, other):
        return Complex(self.i_real+other.i_real, self.i_imaginary+other.i_imaginary)

    def __mul__(self, other):
        return Complex(self.i_real*other.i_real - self.i_imaginary*other.i_imaginary,
                       self.i_real*other.i_imaginary + other.i_real*self.i_imaginary)

    def __str__(self):
        if self.i_imaginary >= 0:
            return f"{self.i_real} + {self.i_imaginary}i"
        else:
            return f"{self.i_real} - {abs(self.i_imaginary)}i"


answer = input("Задание 7 (д/н)? ")
if answer == 'д':
    cm_a = Complex(4, -7)
    cm_b = Complex(2, 3)
    cm_c = Complex(-2, -1)

    print(f"\t({cm_a}) + ({cm_b}) = {cm_a+cm_b}")
    print(f"\t({cm_a}) * ({cm_b}) = {cm_a*cm_b}")

    print(f"\t({cm_b}) + ({cm_c}) = {cm_b+cm_c}")
    print(f"\t({cm_b}) * ({cm_c}) = {cm_b*cm_c}")
