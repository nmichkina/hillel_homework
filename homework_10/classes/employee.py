import company


class Employee:
    company = company.name  # attr of class

    def __init__(self, name: str, age: int, salary: int):  # attr of instance
        self.name = name
        self.age = age
        self.salary = salary
        self.company = Employee.company
        self.address = []
        self.bonus = None
