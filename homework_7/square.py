"""
Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення : периметр квадрата,
площа квадрата та діагональ квадрата. Надрукуйте їх
"""
import math

def square(side):
    area = side * side
    perimeter = 4 * side
    diagonal = math.sqrt(side) * area
    return area, perimeter, diagonal


if __name__ == '__main__':
    side = int(input("Введіть сторону "))
    area, perimeter, diagonal = square(side)
    print(square(side))
