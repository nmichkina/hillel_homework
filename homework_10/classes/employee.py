"""
Create a class with a description of the worker. Any worker or employees.
"""


class Employee:
    company = "Toshiba"  # attribute of class

    def __init__(self, name: str, age: int, salary: int):  # attribute of instance
        self.name = name
        self.age = age
        self.salary = salary
        self.company = Employee.company
        self.address = []
        self.bonus = None

    def showname(self):
        print("Employee name is: " + self.name)


obj = Employee("John", 18, 500)
obj.showname()
