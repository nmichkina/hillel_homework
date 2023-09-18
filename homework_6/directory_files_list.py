"""
Написати програму, яка просканує кореневу папку вашого проєкту, збереже у файл files_size.txt назви та розмір файлів,
і надрукує назву найбільшого файлу та його розмір.
"""

import os

path = r"C:\Users\emgso\PycharmProjects\hillel_homework"
file = "files_size.txt"

fun = lambda x: os.path.isfile(os.path.join(path, x))
files_list = filter(fun, os.listdir(path))

size_of_file = [
    (f, os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]

with open(os.path.join(path, file), 'w') as fp:
    for f, s in size_of_file:
        fp.write("{} : {}MB ".format(f, round(s / (1024 * 1024), 3)))

print(max(size_of_file))
pass



#os.remove(file)