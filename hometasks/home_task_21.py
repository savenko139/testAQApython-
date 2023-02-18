"""

Написать класс Timer для измерения времени выполнения кода.

Прошедшее время должен возвращать в аттрибуте elapsed_time.

Класс должен применяться как контекстный менеджер.

У класса должен быть метод reset.

Если между использованием контекстного менеджера вызывался метод reset, прошедшее время должно считаться заново.

Если метод reset не вызывался, в elapsed_time должно быть сохранено время выполнения всех фрагментов кода обернутых
контекстным менеджером.

"""


import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0
        self.last_time = None

    def __enter__(self):
        self.last_time = time.monotonic()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time += time.monotonic() - self.last_time

    def reset(self):
        self.elapsed_time = 0
        self.last_time = None


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)
