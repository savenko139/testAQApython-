# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

# a = int(input('Enter number А: '))
#
# b = int(input('Enter number B: '))
#
# c = int(input('Enter number C: '))
#
# if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
#     print('yes')
# else:
#     print ('no')


# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.

# a = int(input('Enter number А: '))
#
# b = int(input('Enter number B: '))
#
# c = int(input('Enter number C: '))
#
# max = int(max(a, b, c)) # Я бы в данном случае переменную назвал немного по другому, например max_num
#
# print(max)


# Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

a = int(input('Enter number А: '))

b = int(input('Enter number B: '))

for i in a and b:
    if i % 2 == 0:
     print(a + b)
else:
    print('end')
# print( int(sum(range a, b, 2)))