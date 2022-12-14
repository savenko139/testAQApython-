"""

Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number
является степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.

Пример:

is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256

is_power_of_two(125) # 'no' потому что это не степень двойки

"""

# def is_power_of_two(number: int):
#     i = 0
#     while 2**i < number:
#         i += 1
#     if 2**i == number:
#         return 'YES'
#     else:
#         return 'NO'


def is_power_of_two2(number: int):
    if number%1:
        return 'NO'
    if number>2:
        return is_power_of_two2(number/2)
    if number:
        return 'YES'
    return 'NO'


