"""
написати власну функцію map, використовуючи callback
"""

numbers = ("123", "2587", "3124", "454896")


def cb_list_length(l):
    print("Length of digits in the list are :", l)


def print_dig_length(numbers, callback):
    for n in numbers:
        callback(len(n))


if __name__ == '__main__':
    print_dig_length(numbers, cb_list_length)
