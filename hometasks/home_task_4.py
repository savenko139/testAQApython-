
"""Вывести треугольник #1 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 0

print('Треугольник №1')

while n > c:
    print('*' * n)
    n -= 1

"""Вывести треугольник #2 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 1

print('Треугольник №2')

while c <= n:
    print('*' * c)
    c += 1

# Задание со звездочкой:

""" Вывести треугольник #3 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
i = 0

print('Треугольник №3')

while i < n:
    print(' ' * i + '*' * (n - i))
    i += 1

"""Вывести треугольник #4 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 0

print('Треугольник №4')

while c < n:
    c += 1
    print(' ' * (n - c) + '*' * c)
