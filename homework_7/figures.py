"""
Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
Ця функція намалює простий прямокутник заданої висоти та ширини, використовуючи character для друку ліній
"""


def display_box(width: int, height: int, character="*"):
    print(character * width)
    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)
    print(character * width)


if __name__ == '__main__':
    print(display_box(5, 5))
