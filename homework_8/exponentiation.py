"""
Створіть функцію, яка може повертати квадрати парних чисел у діапазоні від 0 до 1000000000 включно. Рішення має
працювати і не фрізити комп’ютер.
"""


def gen_range(range_num):
    for num in range(range_num):
        if (num % 2) == 0:
            print(pow(num, 2))
        else:
            pass
        yield num


gen = gen_range(10000000)
print(next(gen))
for i in gen:
    print(i)
