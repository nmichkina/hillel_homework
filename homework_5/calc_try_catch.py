"""
Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з
числа, оператора (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).

 - Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
 - Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
 - Якщо введені числа не можуть бути float спіймайте ValueError
 - Також ловіть помилку при діленні на 0
 - В кожній спійманій помилці друкуйте пояснення, що пішло не так
 - За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором,
якщо введені не вірні дані
 - Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
 - Результат виконання формули - float число з двома знаками після крапки
"""
class FormulaError(Exception):
    pass

class WrongOperatorError(Exception):
    pass

print('Калькулятор ділення або множенння двох чисел')
count = 3
while count != 0:
    try:
        first_number = int(input("Введіть перше число: "))
        second_number = int(input("Введіть друге число: "))
        operation = int(input("Введіть операцію (1 для множення, 2 для ділення): "))
        formula = [first_number,' ',operation,' ',second_number]

        if operation not in [1,2]:
            raise WrongOperatorError
        elif int(len(formula)) != 5:
            raise FormulaError
        elif type(first_number) != int:
            raise ValueError
        elif type(second_number) != int:
            raise ValueError

        if operation == 1:
            mult_result = float(first_number * second_number)
            print("Дорівнює: {} * {} = {}".format(first_number,second_number,mult_result))

        elif operation == 2:
            dev_result = float(first_number / second_number)
            print("Дорівнює: {} / {} = {}".format(first_number,second_number,dev_result))
        break

    except ZeroDivisionError as error:
        print(error)
        print("На нуль ділити не можна!")

    except ValueError as error:
        print(error)
        print("Введіть ціле число")

    except FormulaError as error:
        print(error)
        print("Введіть два числа та оператор згідно інструкції")

    except WrongOperatorError as error:
        print(error)
        print("Невірний оператор")

    finally:
        print("Спроба номер:", count)

    count -= 1