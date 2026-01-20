# Write a Python program to implement an Employee Management System using Object-Oriented Programming.
# Create two classes:
 
# Date to store day, month, and year
 
# Employee to store employee name, salary, and joining date
 
# Use a list to store multiple Employee objects.
# Provide a menu-driven program that allows the user to:

# 1. Add employee details
# 2. Display all employee details along with their joining dates
# 3. Exit

EmployeeList = []

def menu():
    print('Enter 1 to add Employee Detail')
    print('Enter 2 to Display0 Employee Detail')


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Employee:
    def __init__(self, name, salary, joiningDate):
        self.name = name
        self.salary = salary
        self.joiningDate = joiningDate

while True:
    menu()
    option = int(input('Enter Option : '))

    match option:
        case 1:
            name = input('Enter Name of Employee: ')
            salary = int(input('Enter salary of Employee: '))

            print('Enter Joining Date of Employee: ')
            day = input('Day   : ')
            month = input('Month : ')
            year = input('Year  : ')

            joiningDate = Date(day, month, year)
            e1 = Employee(name, salary, joiningDate)

            EmployeeList.append(e1)

        case 2:
            for i in EmployeeList:
                 print('Name         : ', i.name)
                 print('Salary       : ', i.salary)
                 print('Joining Date D/M/Y : ', i.joiningDate.day, i.joiningDate.month, i.joiningDate.year, end = '\n')
        case 3:
            break
    
