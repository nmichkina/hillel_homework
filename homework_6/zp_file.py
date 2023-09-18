"""
1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату
(курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv
"""


import csv

rows = []
currency = 37

with open("test_file.csv", 'r+') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append([int(var) * currency if var.isdigit() else var for var in row])

with open("salaries_uah.csv", 'w+') as file:
    write = csv.writer(file)
    write.writerows(rows)
