
"""Вывести треугольник #1 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 0

while n > c:
    print('*' * n)
    n -= 1

"""Вывести треугольник #2 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 1

while c <= n:
    print('*' * c)
    c += 1

# Задание со звездочкой:

""" Вывести треугольник #3 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
i = 0

while i < n:
    print(' ' * i + '*' * (n - i))
    i += 1

"""Вывести треугольник #4 с шириной N с помощью цикла while"""

n = int(input('Enter width of triangle: '))
c = 0

while c < n:
    c += 1
    print(' ' * (n - c) + '*' * c)
