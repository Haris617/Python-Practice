# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
# class Employee:
#     def __init__(self, name, salary, joiningDate):
#         self.name = name
#         self.salary = salary
#         self.joiningDate = joiningDate
#
#

class Person:
    def __init__ (self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

def menu():
    print('Press 1 to Create a Object')
    print('Press 2 to Print an Object')
    print('Press 3 to Update an Object')

PersonList = []

while True:
    menu()
    Option = int(input('Enter your choice: '))
    match Option:
        case 1:
            name = str(input('Enter your name: '))
            age = int(input('Enter your age: '))
            ID = input('Enter your ID: ')

            for p in PersonList:
                if ID == p.ID:

                    print('ID Already Exists')
                    break;

            P1 = Person(name, age, ID)
            print('Object Created')
            PersonList.append(P1)

        case 2:
            for i, p in enumerate(PersonList):
                print(f'{i}. {p.name}, {p.age}, {p.ID}')

        case 3:
            tempID = input('Enter your ID: ')
            found = False

            for i, p in enumerate(PersonList):
                if tempID == p.ID:
                    found = True

                    print('1. Update Name')
                    print('2. Update Age')
                    print('3. Update ID')

                    option = int(input('Enter your choice: '))

                    match option:
                        case 1:
                            p.name = str(input('Enter your name: '))

                        case 2:
                            p.age = int(input('Enter your age: '))

                        case 3:
                            p.ID = input('Enter your ID: ')

                    print('Object Updated')
                    break;

            if not found:
                print('Invalid ID')
