"""
Create a class describing any company. For example, Toshiba or Apple
"""


class Company:
    company = 'Toshiba'  # attribute of class

    def __init__(self, companytype: str, address: str):  # attribute of instance
        self.companytype = companytype
        self.address = address

    def show(self):
        print("Company name is: " + Company.company + " and company type is: " + self.companytype)


obj = Company("Product", "Haifa")
obj.show()
