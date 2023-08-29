"""if elif else"""

# number_1 = 10
# number_2 = 5
#
# if (number_1 * number_2) > 10:
#     print('if True')
#     if (number_1 * number_2) > 20:
#         print('mult of number_1 and number_2 is greater then 20')
# elif (number_1 + number_2) == 10:
#     print('1 elif True')
# elif number_1 == 10:
#     print('2 elif True')
# else:
#     print('False')


secret_number = 8
your_number = input('Вгадай число! Введи свій варіант: ')

if int(your_number) < secret_number:
    print('sercret is bigger')
elif int(your_number) > secret_number:
    print('sercret is lower')
elif int(your_number) == secret_number:
    print('Hurray you are winner')


