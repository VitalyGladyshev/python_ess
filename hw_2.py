"""
Основы Python
ДЗ 2 Гладышев ВВ
"""

import random

# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

answer = input("Задание 1 (д/н)? ")

if answer == 'д':
    dif_types_list = [12, 14., "str", complex(3, 4), [2, 4, 5], {5, 6, 7}, (2, 3, 4), {"2": 2, "3": 3}]

    for el in dif_types_list:
        print(f"Элемент: {el} тип: {type(el)}\n")

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

answer = input("Задание 2 (д/н)? ")

if answer == 'д':
    in_list = []
    print("Введите элемент списка или слово 'стоп' для завершения ввода:")
    while len(in_list) < 1 or in_list[-1] != "стоп":
        in_list.append(input(">> "))
    in_list = in_list[:-1]
    print(f"Исходный список: {in_list}")

    len_add = int(len(in_list) // 2 * 2)
    in_list[1:len_add:2], in_list[0:len_add:2] = in_list[0:len_add:2], in_list[1:len_add:2]
    print(f"Результат: {in_list}\n")

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

answer = input("Задание 3 (д/н)? ")

if answer == 'д':
    month_num = 0
    while 1 > month_num or month_num > 12:
        month_num = int(input("Введите номер месяца: "))

    season_list = []
    season_list.extend([*["зима"] * 2, *["весна"] * 3, *["лето"] * 3, *["осень"] * 3, *["зима"]])
    print(f"Месяц сезона: {season_list[month_num - 1]} (list)")
    season_dict = dict(zip(range(1, 13), season_list))
    print(f"Месяц сезона: {season_dict[month_num]} (dictionary)\n")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

answer = input("Задание 4 (д/н)? ")

if answer == 'д':
    income_str = str(input("Введите строку из нескольких слов, разделённых пробелами: "))
    for i, w in enumerate(income_str.split()):
        print(f"{i + 1} {w[:10]}")
    print("\n")

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

answer = input("Задание 5 (д/н)? ")

if answer == 'д':
    rating = sorted([random.randint(1, 50) for _ in range(25)], reverse=True)
    print(f"Исходная невозрастающая последовательность:\n{rating}")

    num = None
    while num is None:
        try:
            tmp = int(input("Введите натуральное число: "))
        except ValueError:
            print("Некорректный ввод!")
        else:
            num = tmp

    if num > rating[0]:
        rating.insert(0, num)
    elif num < rating[-1]:
        rating.append(num)
    elif num in rating:
        rating.insert((rating[::-1].index(num) + 1) * -1, num)
    else:
        num_sr = num
        while num_sr not in rating:
            num_sr -= 1
        rating.insert(rating.index(num_sr), num)

    print(f"Результат: {rating}")

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

answer = input("Задание 6 (д/н)? ")

if answer == 'д':

    def get_cor_num(str_inv: str) -> int:
        num_tmp = None
        while num_tmp is None:
            try:
                i_tmp = int(input(str_inv))
            except ValueError:
                print("Некорректный ввод!")
            else:
                num_tmp = abs(i_tmp)
        return num_tmp


    products_list = []
    prod_param_list = ('название', 'цена', 'количество', 'eд')
    i_prod_ind = 0
    print("Введите новый товар или слово 'стоп' для завершения ввода:")
    while True:
        s_name = str(input("Введите имя товара (или 'стоп'): "))
        if s_name == "стоп":
            break
        i_price = get_cor_num("Введите цену товара: ")
        i_num_prod = get_cor_num("Введите количество товара: ")
        s_units_meas = str(input("Введите единицы измерения: "))
        print("")
        new_prod_dict = {prod_param_list[0]: s_name,
                         prod_param_list[1]: i_price,
                         prod_param_list[2]: i_num_prod,
                         prod_param_list[3]: s_units_meas}

        products_list.append((i_prod_ind, new_prod_dict))
        i_prod_ind += 1

    print(f"База товаров: {products_list}")

    summarise_dict = {prod_param_list[0]: [],
                      prod_param_list[1]: [],
                      prod_param_list[2]: [],
                      prod_param_list[3]: []}

    for el in products_list:
        for p_p in prod_param_list:
            summarise_dict[p_p].append(el[1][p_p])

    print(f"Сводные данные: {summarise_dict}")
