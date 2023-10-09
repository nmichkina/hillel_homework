"""
Створіть декоратор, який повертає результат функції. а також час за який вона виконана. Підсказка (для фіксації часу
імпортуйте модуль time:  import time)
"""

import time


def my_decorator(func):
    def wrapper(a, b):
        start_time = time.time()
        result = func(a, b)
        print(time.time() - start_time)
        return result

    return wrapper


@my_decorator
def sum_of_two(a, b):
    return a + b


print(sum_of_two(3458256325412, 48569325485632))
