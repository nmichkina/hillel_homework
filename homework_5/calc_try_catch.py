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
while count!= 0:
    try:
        first_number = float(input("Введіть перше число: "))
        second_number = float(input("Введіть друге число: "))
        operation = int(input("Введіть операцію (* або /): "))
        formula = first_number+' '+operation+' '+second_number

        if operation != '*' or '/':
            raise WrongOperatorError('Невірний оператор. Допускається тільки множення або ділення')
        elif len(formula) != 3:
            raise FormulaError
        if operation == '*':
            print("Дорівнює: {} * {} = {}".format(first_number,second_number,first_number*second_number))

        elif operation == '/':
            try:
                print("Дорівнює: {} / {} = {}".format(first_number,second_number,first_number/second_number))
                if second_number == 0:
                    except:
                    print("На нуль ділити не можна!")


    count -= 1