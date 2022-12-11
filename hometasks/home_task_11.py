
"""

1. Написать функцию, которая возвращает слуайную строку заданной длины.

Строка должна состоять из больших и маленьких латинских букв и цифр.

"""


# def get_random_string(length: int) -> str:
#     import random
#     values = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#               81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
#               110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
#     gen_list = random.choices(values, k=length)
#     res = []
#     for i in gen_list:
#         res.append(str(chr(i)))
#     random_str = ''.join(res)
#     return random_str

def get_random_string(length: int) -> str:
    import random
    numbers = [i for i in range(48, 58)]
    chars_upper = [k for k in range(65, 90)]
    chars_lower = [g for g in range(100, 123)]
    final = numbers + chars_upper + chars_lower
    gen_list = random.choices(final, k=length)
    res = []
    for l in gen_list:
        res.append(str(chr(l)))
    random_str = ''.join(res)
    return random_str

