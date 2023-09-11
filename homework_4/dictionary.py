"""
Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення). Виведіть
по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
Виведіть словник на екран.
"""

language_dict = {
    'Python': 'Guido van Rossum',
    'Java' : 'James Gosling',
    'C': 'Dennis Ritchie'
}
for key, value in language_dict.items():
    print('My favorite programming language is ', key, 'It was created by ', value)

language_dict.popitem()
print(language_dict)