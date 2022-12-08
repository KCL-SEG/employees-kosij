"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, hours_worked=None, salary=None, bonus_commission=0, contract_commission=0, commission_per_contract=0):
        self.name = name
        self.contract_type = contract_type
        self.hours_worked = hours_worked
        self.salary = salary
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        # Calculate the contract pay based on the contract type
        if self.contract_type == 'salary':
            contract_pay = self.salary
        else:
            contract_pay = self.hours_worked * self.salary

        # Calculate the commission pay based on the presence of any commission
        if self.bonus_commission:
            commission_pay = self.bonus_commission
        elif self.contract_commission:
            commission_pay = self.contract_commission * self.commission_per_contract
        else:
            commission_pay = 0

        # Return the total pay, which is the sum of the contract pay and the commission pay
        return contract_pay + commission_pay

    def __str__(self):
        # Initialize the string with the employee's name
        string = self.name

        # Add information about the contract type and the pay calculation
        if self.contract_type == 'salary':
            string += ' works on a monthly salary of {}'.format(self.salary)
        else:
            string += ' works on a contract of {} hours at {}/hour'.format(
                self.hours_worked, self.salary)

        # Add information about the presence of any commission and the pay calculation
        if self.bonus_commission:
            string += ' and receives a bonus commission of {}'.format(
                self.bonus_commission)
        elif self.contract_commission:
            string += ' and receives a commission for {} contract(s) at {}/contract'.format(
                self.contract_commission, self.commission_per_contract)

        # Add the total pay calculation to the string
        string += '. Their total pay is {}.'.format(self.get_pay())

        return string


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie', 'salary', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hours_worked=100, salary=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee', 'salary', salary=3000, contract_commission=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan', 'hourly', hours_worked=150, salary=25, contract_commission=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie', 'salary', salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', hours_worked=120, salary=30, bonus_commission=600)
