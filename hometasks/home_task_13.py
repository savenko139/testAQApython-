"""

13. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных
из элементов итерируемых объектов одного индекса.

Функция также должна принимать параметры с дефолтными значениями:

full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной

default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default

"""


def custom_zip(*sequences, full=False, default=None):
    def min_len(*args):
        return len(sorted(args, key=len)[0])        #Вычисляем минимальную длину последовательности

    def max_len(*args):                             #Вычисляем максимальную длину последовательности
        max_len_seq = None
        for i in args:
            if max_len_seq is None or len(i) > max_len_seq:
                max_len_seq = len(i)
        return max_len_seq

    if not full:                                    #Параметр по дефолту (склеиваем по минимальной длине)
        res_len = min_len(*sequences)
        result1 = []
        for i in range(res_len):
            temp1 = []
            for iter in sequences:
                temp1.append(iter[i])
            result1.append(tuple(temp1))
        return result1

    if full:                                        #Параметр True (склеиваем по максимальной длине последовательности)
        res_len = max_len(*sequences)
        result2 = []
        for i in range(res_len):
            temp2 = []
            for iter in sequences:
                if i < len(iter):
                    temp2.append(iter[i])
                else:
                    temp2.append(default)           #Условие, при котором заполняем указанным значением недостающие элементы в кортеж
            result2.append(tuple(temp2))
        return result2


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7, 12, 32, 17]
seq3 = [1, 2, 9]



print(custom_zip(seq1, seq2, seq3, full=True, default='test'))


