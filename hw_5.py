"""
Основы Python
ДЗ 5 Гладышев ВВ
"""

import random

text_dir = "./texts/"

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

answer = input("Задание 1 (д/н)? ")
if answer == 'д':
    try:
        with open(text_dir + "text_for_t1.txt", 'w') as new_file:
            print("\tВводите строки для записи в файл (выход - пустая строка):\n")
            while True:
                new_line = input()
                if new_line == "":
                    break
                new_file.write(new_line+"\n")

        with open(text_dir + "text_for_t1.txt") as read_file:
            while True:
                read_line = read_file.readline()
                if read_line == "":
                    break
                print(read_line, end='')
    except IOError:
        print("\tОшибка открытия файла!")
    print()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

answer = input("Задание 2 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t2.txt") as read_file:
            all_read_lines = read_file.readlines()
            for num, line in enumerate(all_read_lines):
                print(f"\tВ строке {num+1}: {len(line.split())} слов(а)")
            print(f"\tВсего: {len(all_read_lines)} строк(и)\n")
    except IOError:
        print("\tОшибка открытия файла!\n")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
"""

answer = input("Задание 3 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t3.txt") as read_file:
            f_average_salary = 0
            all_read_lines = read_file.readlines()
            for line in all_read_lines:
                s_name, salary = line.split()
                salary = float(salary)
                f_average_salary += salary
                if salary < 20000:
                    print(f"\t{s_name} {salary}")
            if len(all_read_lines) > 0:
                f_average_salary /= len(all_read_lines)
                print(f"\tСредняя зарплата: {f_average_salary:.2f}\n")
    except IOError:
        print("\tОшибка открытия файла!\n")

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

answer = input("Задание 4 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t4.txt") as read_file:
            with open("texts/text_res_t4.txt", "w") as write_file:
                number_words_list = ["Один", "Два", "Три", "Четыре"]
                all_read_lines = read_file.readlines()
                for num, line in enumerate(all_read_lines):
                    if len(line):
                        words = line.split()
                        print(f"{number_words_list[num]} {words[1]} {words[2]}", file=write_file)
                print("\tГотово\n")
    except IOError:
        print("\tОшибка открытия файла!\n")

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

answer = input("Задание 5 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t5.txt", "w") as write_file:
            for _ in range(10):
                write_file.write(str(random.randint(1, 101)) + " ")
        with open("texts/text_for_t5.txt") as read_file:
            read_line = read_file.readline()
            print("\t" + read_line)
            res_sum = 0
            for str_number in read_line.split():
                res_sum += int(str_number)
            print(f"\tСумма: {res_sum}\n")
    except IOError:
        print("\tОшибка открытия файла!\n")

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и 
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

answer = input("Задание 6 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t6.txt") as read_file:
            res_dict = {}
            all_read_lines = read_file.readlines()
            for line in all_read_lines:
                if len(line):
                    subject = line.split()
                    hours_sum = 0
                    for hours in subject[1:]:
                        if len(hours) > 1:
                            hours_sum += int(hours.split('(')[0])
                    res_dict[subject[0]] = hours_sum
            print(f"\t{res_dict}\n")
    except IOError:
        print("\tОшибка открытия файла!\n")

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

answer = input("Задание 7 (д/н)? ")
if answer == 'д':
    pass
