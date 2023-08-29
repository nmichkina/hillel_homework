'''Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2. Написати програму, яка
порахує об'єм і температуру суміші, що вийшла. Обчислюється за формулою (v1 * t1 + v2 * t2) / (v1 + v2)
Всі параметри виводяться в консолі, вивести обʼєм та температуру'''

water_value_1 = input("Введіть, будьласка, перший об'єм води в літрах")
water_value_2 = input("Введіть, будьласка, другий об'єм води в літрах")
water_temperature_1 = input("Введіть, будьласка, першу температуру води в градусах цельсію")
water_temperature_2 = input("Введіть, будьласка, другу температуру води в градусах цельсію")
water_temperature = (float(water_value_1) * float(water_temperature_1) + float(water_value_2) *
                     float(water_temperature_2)) / (float(water_value_1) + float (water_value_2))
water_value = float(water_value_1) + float(water_value_2)

print("Температура змышаної води становить: ", water_temperature)
print("Об'єм змішаної води становить: ", water_value)