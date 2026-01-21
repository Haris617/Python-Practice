# Polymorphism

class Employee:
    def calculatePay(self):
        print("Pay not defined")

class FullTime(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculatePay(self):
        return self.salary


class PartTime(Employee):
    def __init__(self, hoursWorked, hourlyPay):
        self.hoursWorked = hoursWorked
        self.hourlyPay = hourlyPay

    def calculatePay(self):
        return self.hoursWorked * self.hourlyPay


class Contractor(FullTime, PartTime):
    def __init__(self, salary, hoursWorked, hourlyPay, contractBonus):
        FullTime.__init__(self, salary)
        PartTime.__init__(self, hoursWorked, hourlyPay)
        self.contractBonus = contractBonus

    def calculatePay(self):
        # Polymorphism: same method name, different behavior

        totalPay = FullTime.calculatePay(self) + PartTime.calculatePay(self) + self.contractBonus
        print(f"Contractor Pay = {totalPay}")


c = Contractor(10,10,10,10)

print(PartTime.calculatePay(c))
print(FullTime.calculatePay(c))
c.calculatePay()
