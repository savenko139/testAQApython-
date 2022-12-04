"""

Написать декоратор call_times, который будет принимать в качестве параметра file_name, считать количество
вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'

"""

def call_times(filename):
    def counter(func):
        def inner(*args, **kwargs):
            inner.count += 1
            result = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(f'{func.__name__} was called {inner.count} times. \n')

            return result

        inner.count = 0

        return inner

    return counter