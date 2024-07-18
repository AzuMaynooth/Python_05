'''
In this exercise, you are tasked to write a Python program that simulates operations on a school database. The program should enable the creation
 of three types of users (student, teacher, and homeroom teacher), as well as manage them.

1. Write a program that displays available commands upon launch. The commands are: create, manage, end.

2. Handle each command uniquely:
  - 'create': The program should start the user creation process.
  - 'manage': The program should start the user management process.
  - 'end': Terminate the program.

User Creation Process:

1. Prompt for a user type to create: student, teacher, homeroom teacher, end. After creating a user (except for 'end'), the menu should be displayed again.
  - 'student': Prompt for the student's first and last name (as one or two variables, depending on your design) and the class name (e.g., "3C").
  - 'teacher': Prompt for the teacher's first and last name (as one or two variables, depending on your design),
  the subject they teach, and the names of the classes they teach, until an empty line is entered.
  - 'homeroom teacher': Prompt for the homeroom teacher's first and last name (as one or two variables, depending on your design),
   and the name of the class they lead.
  - 'end': Return to the main menu.

User Management Process:

1. Prompt for an option to manage: class, student, teacher, homeroom teacher, end. After managing an option (except for 'end'),
the menu should be displayed again.
  - 'class': Prompt for a class to display (e.g., "3C"), the program should list all students in the class and the homeroom teacher.
  - 'student': Prompt for a student's first and last name, the program should list all the classes the student attends and the teachers of these classes.
  - 'teacher': Prompt for a teacher's first and last name, the program should list all the classes the teacher teaches.
  - 'homeroom teacher': Prompt for a homeroom teacher's first and last name, the program should list all students the homeroom teacher leads.
  - 'end': Return to the main menu.

Hints:

- Use loops and conditionals to control the flow of your program.
- Keep track of users and their attributes in suitable data structures.
- Handle possible errors like entering a user that doesn't exist in the database.
'''


class student:
    def __init__(self, name, surname, clase):
        self.name = name
        self.surname = surname
        self.clase = clase

    def __str__(self):
        return f"[{self.name} {self.surname} {self.clase} ]"
        

class teacher:
    def __init__(self, name, surname, clase, subject):
        self.name = name
        self.surname = surname
        self.clase = clase
        self.subject = {self.subject}

    def __str__(self):
        return f"[{self.name} {self.surname} {self.clase} {self.subject} ]"


def end():
    print('Program is terminated.')
    exit()


def creation_process():

    obj = None
    slc = input('What do you want to create?\n'
               '1) Student\n'
               '2) Teacher\n'
               '3) Homeroom teacher\n'
               '4) end\n')

    obj = int(input("Please add option: "))

    global students_lst
    global teachers_lst
    #global students_lst
    try:

        if obj == 'Student':

            name = input("Add student name")
            surname = input("Add surname name")
            clase = input("Add student class")

            students = student(name, surname, clase)
            students_lst.append(students)

        elif obj == 'Teacher':
            name = input("Add teacher name")
            surname = input("Add surname name")
            clase = input("Add teacher class")
            subject = input("Add subject ")

            teacher(name, surname, clase, subject)
        elif obj == ' homeroom teacher':
            print("home")
        else:
            print("Tiene q volver al main menu")


    except ValueError:
        print('Please add string value. \n')

def managament_process():

    obj = None
    slc = input('What do you want to manage?\n'
                '1) Student\n'
                '2) Teacher\n'
                '3) Homeroom teacher\n'
                '4) end\n')
    obj = int(input("Please add option: "))

    if obj == 'Student':
        print('Manage student')

    elif obj == 'Teacher':
        print('Manage tecaher')

    #elif obj == 'Homeroom teacher':
        #print('Manage home stu')

    else:
        print("Tiene q volver al main menu")


def cuerpazo():

    students_lst = []
    teachers_lst = []


    comando = None

    while comando != 'end':

        op = input('What do you want to do?\n'
                   '1) Create\n'
                   '2) Manage\n'
                   '3) end\n')

        comando = abs(int(input('Enter the amount: ')))

        if op == 'Create':
            print('Estas creando')
            creation_process()

        elif op == 'Manage':
            print('Estas manegando')
            managament_process()

        elif op == 'end':
            print('Te sales')
            end()
        else:
            print('Invalid input, try again, please.\n')