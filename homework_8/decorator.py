"""
Створіть декоратор, який виводить в консоль назву викликаної функції. Наприклад, створіть пару функцій для арифметичних
 операцій підсумовування та множення. Під час виклику цих функцій має бути повернутий результат операції, а ім’я
 викликаної функції має відображатися на консолі разом із результатом. Маленька підказка (__name__)
"""


def my_decorator(func):
    def wrapper(a, b):
        print(func.__name__)
        result = func(a, b)
        return result
    return wrapper


@my_decorator
def sum_of_two(a, b):
    return a + b


@my_decorator
def mult_of_two(a, b):
    return a * b


print(sum_of_two(3, 4))
print(mult_of_two(2, 2))
