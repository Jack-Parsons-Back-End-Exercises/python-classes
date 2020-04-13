class Company:

    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def generate_report(self):
        print(f'{self.name} is in the {self.industry} industry and has the following employees:')
        for employee in self.employees:
            print(f'    * {employee.name}')