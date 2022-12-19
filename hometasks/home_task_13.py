"""

3. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных
из элементов итерируемых объектов одного индекса.

Функция также должна принимать параметры с дефолтными значениями:

full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной

default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default

"""

# def custom_zip(*sequences: iterable, full=False, default=None):
#     out = []
#     def shortest_sequence_range(*args):
#         return range(len(sorted(args, key=len)[0]))
#     iters = [iter(i) for i in sequences]
#         for i in shortest_sequence_range(iters))
#             for item in g:
#             print(item)

def custom_zip(*seq, full=False, default=None):
    # if True:
        # def longest_sequence_range(*args):
        #     return range(len(sorted(args, key=len)[0]))
        # iters = [iter(i) for i in shortest_sequence_range(*seq)]

    # else:
        def shortest_sequence_range(*args):
            return range(len(sorted(args, key=len)[0]))
        iters = [iter(seq) for i in shortest_sequence_range(*seq)]
        res = []
        for item in iters:
            res.append(item)
        return res


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

# print(list(zip(seq1, seq2)))


def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))

iters = ((seq1[i], seq2[i]) for i in shortest_sequence_range(seq1, seq2))

res = []

for item in iters:
    res.append(item)

print(res)
