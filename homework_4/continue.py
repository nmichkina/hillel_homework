"""
The list of names is given: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

Using the continue statement, print only the correct names to the console
"""

names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
names_only = []
index = 0
while index < len(names):
    name = names[index]
    index += 1
    if isinstance(name, str):
        names_only.append(name)
    else:
        continue

    print(names_only)

