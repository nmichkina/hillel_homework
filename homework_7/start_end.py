"""
Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.
"""


def sum_range(start, end):
    if start <= end:
        return sum(range(start, end))
    else:
        return sum(range(end, start))


if __name__ == '__main__':
    start = int(input("Введіть мінімальне число "))
    end = int(input("Введіть максимельне число "))
    print(sum_range(start, end))
