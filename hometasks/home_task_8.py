
"""
Задание 1
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""

def change(lst: list):
    if len(lst) < 2:
        print('В списке должно быть минимум 2 элемента')
    else:
        lst[-1], lst[0] = lst[0], lst[-1]
        print(lst)

"""
Задание 2
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент 
списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать 
правилам задания ключей в словарях.

"""

def to_dict1(lst):                     # Сначала придумал такой вариант
    new_dict = {}
    for i in lst:
        new_dict.update({
            i:i
        })
    return new_dict

def to_dict2(lst):                     # Но потом поигрался и нашел еще один способ (чуть проще как по мне)
    new_dict2 = {i: i for i in lst}
    return new_dict2



"""
Задание 3
Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» 
включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

"""

def sum_range(start: int, end: int) -> int:
    sumch = 0
    if start > end:
        for i in range(end, start+1):
            sumch += i
    else:
        for i in range (start, end+1):
            sumch += i
    print(sumch)


"""
Задание 4
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно 
последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число)
"""

def read_last(lines: int, file: str):
    if lines <= 0:
        print('Enter number > 0')
    else:
        try:
            with open(file) as text:
                file_lines = text.readlines()[-lines:]
            for line in file_lines:
                print(line.strip())
        except FileNotFoundError as e:
            print(e)