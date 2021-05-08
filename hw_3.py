"""
Основы Python
ДЗ 3 Гладышев ВВ
"""


# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(divisible: str, divisor: str) -> float or None:
    """
    Функция выполняет деление параметров и возвращает результат.
    Проверятся возможность приведения параметров к float.
    Обрабатывается возможность деления на 0

    :param divisible: делимое
    :param divisor: делитель
    :return: результат деления или None
    """

    division_res = None
    try:
        divisible = float(divisible)
        divisor = float(divisor)
    except ValueError:
        print(f"Ошибка приведения параметров к float!")
    else:
        try:
            division_res = divisible / divisor
        except ZeroDivisionError:
            print(f"Деление на ноль. Делитель равен нулю!")
    return division_res


answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    str_divisible = input("\nВведите делимое: ")
    str_divisor = input("Введите делитель: ")
    f_div_res = division(str_divisible, str_divisor)
    if f_div_res is not None:
        print(f"Результат деления {str_divisible} на {str_divisor} равен {f_div_res}")


# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def print_user_data(name: str,
                    surname: str,
                    birth_year: str,
                    city: str,
                    email: str,
                    phone: str) -> None:
    """
    Распечатывает строку с данными пользователя

    :param name: имя
    :param surname: фамилия
    :param birth_year: год рождения
    :param city: город проживания
    :param email: электронная почта
    :param phone: номер телефона
    :return: распечатывает строку с данными пользователя
    """
    print(f"Пользователь: {surname} {name} {birth_year} года рождения проживает"
          f" в городе {city}. Телефон: {phone}, email: {email}")


answer = input("\nЗадание 2 (д/н)? ")
if answer == 'д':
    str_name = input("\nВведите имя: ")
    str_surname = input("Введите фамилия: ")
    str_birth_year = input("Введите год рождения: ")
    str_city = input("Введите город проживания: ")
    str_email = input("Введите email: ")
    str_phone = input("Введите телефон: ")

    kwargs = {
        'name': str_name,
        'surname': str_surname,
        'birth_year': str_birth_year,
        'city': str_city,
        'email': str_email,
        'phone': str_phone
    }
    print_user_data(**kwargs)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func_sum(par1: float, par2: float, par3: float) -> float:
    """
    Возвращает сумму наибольших двух параметров

    :param par1: параметр 1
    :param par2: параметр 2
    :param par3: параметр 3
    :return: сумма наибольших двух параметров
    """
    return par1 + par2 + par3 - min(par1, par2, par3)


answer = input("\nЗадание 3 (д/н)? ")
if answer == 'д':
    try:
        f_arg1 = float(input("\nВведите первый аргумент: "))
        f_arg2 = float(input("Введите второй аргумент: "))
        f_arg3 = float(input("Введите третий аргумент: "))
    except ValueError:
        print(f"Ошибка приведения аргументов к float!")
    else:
        print(f"Сумма наибольших двух аргументов: {my_func_sum(f_arg1, f_arg2, f_arg3)}")


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func_exp(num: float, exp: int) -> float:
    """
    Возведение числа num в степень exp

    :param num: возводимое в степень число
    :param exp: показатель степени
    :return: число num в степени exp
    """
    res = num
    for _ in range(abs(exp) - 1):
        res *= num
    if exp == 0:
        return 1.
    elif exp > 0:
        return res
    else:
        return 1 / res


answer = input("\nЗадание 4 (д/н)? ")
if answer == 'д':
    try:
        f_num = abs(float(input("\nВведите действительное положительное число: ")))
    except ValueError:
        print(f"Ошибка приведения аргумента к float!")
    else:
        try:
            i_exp = int(input("Введите показатель степени - целое отрицательное число: "))
        except ValueError:
            print(f"Ошибка приведения аргумента к int!")
        else:
            # if i_exp > 0:
            #     i_exp *= -1
            print(f"Число {f_num} в степени {i_exp}: {my_func_exp(f_num, i_exp)}")

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

answer = input("\nЗадание 5 (д/н)? ")
if answer == 'д':
    f_res = 0
    b_exit = False
    while True:
        income_list = list(input("\nВведите сроку чисел разделённых пробелами (для выхода введите 'стоп'): ").split())
        for el in income_list:
            if el == 'стоп':
                b_exit = True
                break
            try:
                el = float(el)
            except ValueError:
                print(f"Элемент {el} невозможно привести к float он будет проигнорирован!")
            else:
                f_res += el
        print(f"Сумма: {f_res}")
        if b_exit:
            break


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(in_str: str) -> str:
    """
    Принимает слово из маленьких букв и возвращает его же, но с прописной первой буквой

    :param in_str: слово для изменения первой буквы на заглавную
    :return: слово с изменённой первой буквой
    """
    return in_str[0].capitalize() + in_str[1:]


answer = input("\nЗадание 6 (д/н)? ")
if answer == 'д':
    str_res = ''
    inc_list = input("\nВведите строку из слов, разделенных пробелом: ").split()
    for wd in inc_list:
        str_res += (int_func(wd) + ' ')
    print(str_res)
