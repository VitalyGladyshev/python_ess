"""
Основы Python
ДЗ 4 Гладышев ВВ
"""

import sys
from random import randint, randrange
from collections import Counter
from functools import reduce
from typing import Generator, List


# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


def salary_count(f_emp_dev: float, f_rate: float, f_award: float) -> float:
    """
    Функция для вычисления зарплаты сотрудника
    формула: (выработка в часах * ставка в час) + премия

    :param f_emp_dev: выработка в часах
    :param f_rate: ставка в час
    :param f_award: премия
    :return: зарплата
    """
    return f_emp_dev * f_rate + f_award


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    try:
        file, emp_dev, rate, award = sys.argv
        emp_dev = float(emp_dev)
        rate = float(rate)
        award = float(award)
    except ValueError:
        print(f"\nОшибка обработки аргументов!\n")
    else:
        print(f"\nВыработка сотрудника: {emp_dev}\nСтавка в час: {rate}\nПремия: {award}")
        print(f"Заработная плата сотрудника: {salary_count(emp_dev, rate, award)}\n")

# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    rand_list = [randint(1, 10) for _ in range(15)]
    print(f'\nИсходный список: {rand_list}')
    print(f"Результирующий список: "
          f"{[rand_list[i] for i in range(1, len(rand_list)) if rand_list[i] > rand_list[i - 1]]}\n")

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    print(f"\nКратные числа: {[i for i in range(20, 241) if not i % 20 or not i % 21]}\n")

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

answer = input("Задание 4 (д/н)? ")
if answer == 'д':
    rand_list = [randint(1, 10) for _ in range(12)]
    print(f'\nИсходный список: {rand_list}')
    print(f"Результирующий список: {[key for key, val in Counter(rand_list).items() if val == 1]}\n")

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

answer = input("Задание 5 (д/н)? ")
if answer == 'д':
    rand_list = [randrange(100, 1000, 2) for _ in range(3)]
    print(f'\nИсходный список: {rand_list}')
    print(f'Произведение элементов: {reduce(lambda x, y: x * y, rand_list)}\n')


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


def my_counter(start: int) -> Generator[int, None, None]:
    """
    итератор, генерирующий целые числа, начиная с указанного

    :param start: стартовое число
    :return: итератор, генерирующий целые числа, начиная с указанного
    """
    while True:
        yield start
        start += 1


def list_repeat(inc_list: List) -> Generator[int, None, None]:
    """
    итератор, повторяющий элементы некоторого списка, определенного заранее

    :param inc_list: список предопределённых элементов
    :return: итератор, повторяющий элементы некоторого списка, определенного заранее
    """
    while True:
        for el_il in inc_list:
            yield el_il


answer = input("Задание 6 (д/н)? ")
if answer == 'д':
    res_list = []
    for el in my_counter(7):
        res_list.append(el)
        if el > 12:
            break
    print(f"\nСписок сформированный первым генератором: {res_list}")
    print("Циклический вывод первого списка:")
    for i, el_2 in enumerate(list_repeat(res_list)):
        print(f"\t{i + 1}\t{el_2}")
        if i > 15:
            break
    print("")


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.


def fact(i_n: int) -> Generator[int, None, None]:
    """
    Генератор факториалов от 1 до i_n

    :param i_n: до какого числа выводить факториалы
    :return: объект-генератор факториалов
    """
    it: int = 1
    for i in range(1, i_n + 1):
        it *= i
        yield it
    return


answer = input("Задание 7 (д/н)? ")
if answer == 'д':
    print(f"\nВыводим факториалы чисел от 1 до 15:")
    for i_inc, el_fact in enumerate(fact(15)):
        print(f"\t{i_inc + 1}!\t{el_fact}")
