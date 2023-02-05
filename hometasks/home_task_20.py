"""

Написать декоратор skip, которым можно декорировать функции.

Если переданное выражение condition истинное, функция не должна выполнятся, а должна вывестись строка reason.

Если выражение condition ложное, функция должна выполнится.

"""


def skip(condition, reason):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@skip(condition=True, reason='Skipped because of bug')
def sum_range(start: int, end: int) -> int:
    sumch = 0
    if start > end:
        for i in range(end, start+1):
            sumch += i
    else:
        for i in range (start, end+1):
             sumch += i
        return(sumch)


print(sum_range(2, 3))