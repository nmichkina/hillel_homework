class Employee:
    """
    a class with a description of the worker. Any worker or employees.
    """
    company = "Toshiba"  # attribute of class

    def __init__(self, name: str, age: int, salary: int, emp_position: str):  # attribute of instance
        self.name = name
        self.age = age
        self.salary = salary
        self.__emp_position = emp_position
        self.company = Employee.company
        self._address = []
        self.bonus = None

    def showname(self):
        """
        Shows worker name
        :return: self.name
        """
        print("Employee name is: " + self.name)

    @staticmethod
    def show_high_income_months():
        """
        Shows the high income month
        :return: str
        """
        print('December')

    @classmethod
    def with_bonus(cls, name, age, salary, emp_position, bonus_amount):
        """
        Adding bonus amount to the class
        :param name:
        :param age:
        :param salary:
        :param emp_position:
        :param bonus_amount:
        :return: bonus_amount
        """
        obj_ = cls(name, age, salary, emp_position)
        obj_.bonus = bonus_amount
        return obj_

    @property
    def emp_position(self):
        """
        Returns employee position
        :return: emp_position
        """
        return self.__emp_position

    @emp_position.setter
    def emp_position(self, new_position):
        """
        Set employee position
        :param new_position:
        :return: position
        """
        self.__emp_position = new_position


obj = Employee("Sam", 18, 500, "pm")
obj.showname()
anton = Employee.with_bonus('Anton', 30, 1000, "developer", 100)
print(anton.bonus)
print(anton.emp_position)
print(Employee.show_high_income_months())
