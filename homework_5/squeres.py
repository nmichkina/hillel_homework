"""
Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

Лише за допомогою функцій map, lambda, zip створити та надрукувати словник квадратів цих чисел.

Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
sq_list = []

for number in str_list:
   int_list = [eval(i) for i in str_list]
   sq_list.append(int(number) ** 2)

    print(dict(zip(int_list, sq_list)))