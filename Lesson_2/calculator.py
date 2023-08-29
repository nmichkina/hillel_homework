'''Написать калькулятор с основными операциями(+, -, *, /)
Користувач вводить два числа та арифметичну операцію
Також можна додати перевірку для всіх задач з негативним сценарієм'''

first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))

print("""
Виберіть операцію зі списку:
1. Додавання
2. Віднімання
3. Множення
4. Ділення
""")

operation = int(input("Введіть номер операції: "))

if operation == 1:
        print("Дорівнює: {} + {} = {}".format(first_number,second_number,first_number+second_number))
elif operation == 2:
        print("Дорівнює: {} - {} = {}".format(first_number,second_number,first_number-second_number))
elif operation == 3:
        print("Дорівнює: {} * {} = {}".format(first_number,second_number,first_number*second_number))
elif operation == 4:
        try:
            print("Дорівнює: {} / {} = {}".format(first_number,second_number,first_number/second_number))
        except:
            print("На нуль ділити не можна!")
else:
        print("Невірна операція!")