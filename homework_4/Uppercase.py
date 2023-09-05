'''
Існує список з іменами ["john", "marta", "james", "amanda", "marianna"], перетворити рядок, щоб кожне ім'я явно
починалися з великої літери.
'''

names = ["john", "marta", "james", "amanda", "marianna"]
names_capitalized = [name.title() for name in names]
print(names_capitalized)