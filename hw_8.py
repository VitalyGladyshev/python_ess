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


class ExceptionDivZero:
    """
    
    """
    pass


answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    pass

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только
числами. Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExceptionListOfNumbers:
    """

    """
    pass


answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    pass

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
    """

    """
    pass


class OfficeEquipment:
    """

    """
    pass


class Printer(OfficeEquipment):
    """Класс Принтер"""
    pass


class Scanner(OfficeEquipment):
    """Класс сканер"""
    pass


class Copier(OfficeEquipment):
    """Класс копир"""
    pass


answer = input("Задание 4, 5, 6 (д/н)? ")
if answer == 'д':
    pass

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    """Класс Комплексное число"""
    pass


answer = input("Задание 7 (д/н)? ")
if answer == 'д':
    pass
