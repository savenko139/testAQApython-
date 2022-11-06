
"""Задание 1:
Запросить у пользователя 5 чисел и записать их в список"""

print('Задание 1')
values = []

for _ in range (5):
    number = int(input('Enter a value: '))
    values.append(number)

print(values)

"""Задание 2:
Дан список A = [1, 2, 3, 4, 5]
Удалить последнее число из списка"""

print('Задание 2')
A = [1, 2, 3, 4, 5]

print('Список до удаления последнего числа:', A)

A.pop()

print('Список после удаления последнего числа:', A)


"""Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N"""

print('Задание 3')
values = []

for _ in range (10):
    number = int(input('Enter the values for list: '))
    values.append(number)


N = int(input('Enter your number: '))
count = values.count(N)

print(values)               #Вывел список для наглядности
print('Your number repeats {} times in list!'.format(count))

"""Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

print('Задание 4')
N = int(input('Enter N: '))

A = []

for _ in range (N):
    number = int(input('Enter values: '))
    A.append(number)

A.reverse()
print(A)

"""Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C"""

print('Задание 5')
A = []
C = []

for _ in range (5):
    number = int(input('Enter values: '))
    A.append(number)

for i in (A):
    if i > 5:
        C.append(i)

print(A)                    #Вывел список для наглядности
print(C)

"""Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
"""
print('Задание 6')
N = int(input('Enter N: '))
A = []

for _ in range (N):
    number = int(input('Enter values: '))
    A.append(number)

print(A)                    # Решил вывести здесь список для наглядности. Но фактически в этом нет нужды

max_value = A[0]
min_value = A[0]

for i in (A):
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i

print('Maximum value in list A is:', max_value, '!')
print('Minimum value in list A is:', min_value, '!')

"""Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3"""
""""""

print('Задание 7')
text = input('Enter something: ')

import re

count = len(re.findall('\d+',text))
print('Количество чисел:',count)

















