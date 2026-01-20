# Hospital Management System

def menu():
    print('\n', f"{'DOCTOR':*^40}")
    print('1. Add a Doctor')
    print('2. Display all Doctors')
    print(f"{'NURSE':*^40}")
    print('3. Add a Nurse')
    print('4. Display all Nurses')
    print(f"{'PATIENT':*^40}")
    print('5. Add a Patient')
    print('6. Display all Patients')
    print('0. Exit\n')



class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age  = age
        self.gender = gender

    def displayPerson(self):
        print('Name   :', self.name)
        print('Age    :', self.age)
        print('Gender :', self.gender)


class Employee:
    def __init__(self, employeeID, salary):
        self.employeeID = employeeID
        self.salary = salary

    def displayEmployee(self):
        print('Employee ID     :', self.employeeID)
        print('Employee Salary :', self.salary)



class Doctor(Person, Employee):
    def __init__(self, name, age, gender, employeeID, salary, specialization, patientsPerDay):
        Person.__init__(self, name, age, gender)
        Employee.__init__(self, employeeID, salary)

        self.specialization = specialization
        self.patientsPerDay = patientsPerDay

    def addData(self):
        self.name    = input('Enter Doctor Name           : ')
        self.age     = input('Enter Doctor Age            : ')
        self.gender  = input('Enter Doctor Gender         : ')
        self.employeeID = input('Enter Doctor Employee ID    : ')
        self.salary     = input('Enter Doctor Salary         : ')
        self.specialization = input('Enter Specialization        : ')
        self.patientsPerDay = input('Patients Per Day            : ')

        DoctorList.append(self)
        print('Doctor Added Successfully')

    def display(self):
        self.displayPerson()
        self.displayEmployee()
        print('Specialization  :', self.specialization)
        print('Patients/Day    :', self.patientsPerDay)
        print()



class Nurse(Person, Employee):
    def __init__(self, name, age, gender, employeeID, salary, shift, assignedWard):
        Person.__init__(self, name, age, gender)
        Employee.__init__(self, employeeID, salary)
        self.shift = shift
        self.assignedWard = assignedWard

    def addData(self):
        self.name   = input('Enter Nurse Name        : ')
        self.age    = input('Enter Nurse Age         : ')
        self.gender = input('Enter Nurse Gender      : ')
        self.employeeID = input('Enter Nurse Employee ID : ')
        self.salary     = input('Enter Nurse Salary      : ')
        self.shift = input('Enter Nurse Shift       : ')
        self.assignedWard = input('Enter Assigned Ward     : ')

        NurseList.append(self)
        print('Nurse Added Successfully')

    def display(self):
        self.displayPerson()
        self.displayEmployee()
        print('Shift          :', self.shift)
        print('Assigned Ward  :', self.assignedWard)
        print()


class Patient(Person):
    def __init__(self, name, age, gender, patientID, ailment, doctor):
        Person.__init__(self, name, age, gender)
        self.patientID = patientID
        self.ailment = ailment
        self.doctor = doctor

    def addData(self):
        if not DoctorList:
            print('No doctors available. Add doctor first.')
            return

        self.name = input('Enter Patient Name   : ')
        self.age  = input('Enter Patient Age    : ')
        self.gender = input('Enter Patient Gender : ')
        self.patientID = input('Enter Patient ID     : ')
        self.ailment = input('Enter Ailment        : ')

        print('\nAvailable Doctors:')
        for d in DoctorList:
            print(f"ID:{d.employeeID} | Name:{d.name} | Spec:{d.specialization}")

        tempID = input('Enter Doctor Employee ID to assign: ')

        for d in DoctorList:
            if d.employeeID == tempID:
                self.doctor = d
                PatientList.append(self)
                print('Patient Added Successfully\n')
                return

        print('Doctor Not Found')

    def display(self):
        self.displayPerson()
        print('Patient ID :', self.patientID)
        print('Ailment    :', self.ailment)

        if self.doctor:
            print(f'Doctor Assigned : {self.doctor.name} ({self.doctor.specialization})')
        else:
            print('Doctor Assigned : None')
        print()


DoctorList = []
NurseList = []
PatientList = []


while True:
    menu()
    choice = input('Enter Choice: ')

    match choice:
        case '1':
            d = Doctor(None, None, None, None, None, None, None)
            d.addData()
        case '2':
            for d in DoctorList:
                d.display()

        case '3':
            n = Nurse(None, None, None, None, None, None, None)
            n.addData()

        case '4':
            for n in NurseList:
                n.display()

        case '5':
            p = Patient(None, None, None, None, None, None)
            p.addData()

        case '6':
            for p in PatientList:
                p.display()

        case '0':
            print('Exiting...')
            break

        case _:
            print('Invalid Choice')
