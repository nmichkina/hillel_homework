class Company:
    """
    Class that describes the company
    """
    company = 'Toshiba'  # attribute of class

    def __init__(self, company_type: str, address: str):  # attribute of instance
        self.company_type = company_type
        self.address = address

    def show(self):
        """
        returns the class instance
        :return: self
        """
        print("Company name is: " + Company.company + " and company type is: " + self.company_type)


obj = Company("Product", "Haifa")
obj.show()
