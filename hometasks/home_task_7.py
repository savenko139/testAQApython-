"""
Задание 1

Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
"""

f = open('', 'r') # Перед запуском кода нужно добавить файл в директорию и его название в строку кода
data = f.read()
f.close()

import re
numbers = list(map(int, re.findall('\d+',data)))
print(numbers)

"""
Задание 2

Запросить у пользователя текст и записать его в файл data.txt
"""

text = input('Enter your text here: ')

with open('data.txt', 'w') as f:
    f.write(text)


"""
Задание 3

Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
"""

N = int(input('Enter N: '))
numbers = []
for _ in range (N):
    number = int(input('Enter values: '))
    numbers.append(number)

with open('numbers.txt', 'w') as f:
    for item in numbers:
        f.write("%s" % item + ' ')


"""
Задание 4

Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
"""

import random


random_items = [random.randint(1, 100) for _ in range(100)]

with open('random_numbers.txt', 'w') as f:
    for item in random_items:
        f.write("%s\n" % item)

"""
Задание 5

Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
"""

import re

f = open('', 'r') # Перед запуском кода нужно добавить файл в директорию и его название в строку кода
data = f.read()
f.close()

count = len(re.findall('\w+', data))
print('Количество слов в файле: ', count)


"""
Задание 6

Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
"""

import re
with open('') as data: # Перед запуском кода нужно добавить файл в директорию и его название в строку кода
    res = list(map(int, re.findall(r'\d+', ''.join(data.readlines()))))
    print(res)
    print(sum(res))

"""
Задание 7

Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:

'в' - 20 раз

'привет' - 10 раз

'как' - 9 раз

'у' - 7

'world' - 4
"""

import collections
import re

words = list(map(str, re.findall(r'\w+', open('').read()))) # Перед запуском кода нужно добавить файл в директорию и его название в строку кода
c = collections.Counter(words).most_common(5)
print('Наиболее используемые слова в тексте из файла:')
for i in c:
    print((i[0]) + ' - ' + str(i[1]) + ' раз')