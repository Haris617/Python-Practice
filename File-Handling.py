StudentList = []

def menu():
    print('Press 1 to Add Student')
    print('Press 2 to Display Student List')
    print('Press 3 to Search By Id')
    print('Press 5 to Exit')


class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

def addStudent():
    id = input('Enter Id : ')
    name = input('Enter Name : ')
    age = int(input('Enter age : '))
    s = Student(id, name, age)

    try:
        with open("Student_List.txt", "a") as file:
            file.write('{},{},{}\n'.format(id, name, age))

    except Exception as e:
        print('File not Found Error : {}'.format(e))

    print('Student Added')
    return s

def displayStudents():
    try:
        with open("Student_List.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                id, name, age = parts
                print('Id   :', id)
                print('Name :', name)
                print('Age  :', age)
                print('\n')

    except FileNotFoundError:
        print("No student data found.")


def searchById():
    tempId = input('Enter Id to Search : ')
    found = False

    with open("Student_List.txt") as file:
        for line in file:
            parts = line.strip().split(',')

            id, name, age = parts

            if(tempId == id):
                found = True
                print('Id Found')
                print('Id   :', id)
                print('Name :', name)
                print('Age  :', age)
                print('\n')

        if not found:
            print('Id not Found')

while True:
    menu()
    option = int(input())

    match option:
        case 1:
            StudentList.append(addStudent())
        case 2:
            displayStudents()
        case 3:
            searchById()
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid Option")
