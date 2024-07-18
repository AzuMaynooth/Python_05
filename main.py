'''

In this exercise, you are tasked to write a Python program that simulates operations on a school database.
The program should enable the creation of three types of users (student, teacher, and homeroom teacher), as well as manage them.

1. Write a program that displays available commands upon launch. The commands are: create, manage, end.

2. Handle each command uniquely:
  - 'create': The program should start the user creation process.
  - 'manage': The program should start the user management process.
  - 'end': Terminate the program.

User Creation Process:


User Management Process:

1. Prompt for an option to manage: class, student, teacher, homeroom teacher, end.
After managing an option (except for 'end'), the menu should be displayed again.
  - 'class': Prompt for a class to display (e.g., "3C"), the program should list all students in the class and the homeroom teacher.
  - 'student': Prompt for a student's first and last name, the program should list all the classes the student attends
    and the teachers of these classes.
  - 'teacher': Prompt for a teacher's first and last name, the program should list all the classes the teacher teaches.
  - 'homeroom teacher': Prompt for a homeroom teacher's first and last name, the program should list all students
    the homeroom teacher leads.
  - 'end': Return to the main menu.
.
'''

from datetime import datetime
import datetime



'''
Define classes
'''

students_lst = []
teachers_lst = []
homerooms_lst = []


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

class Student(Person):
    def __init__(self, name, surname, classroom):
        Person.__init__(self, name, surname)
        self.classroom = classroom

    def __str__(self):
        return f"[Student: {Person.__str__(self)} {self.classroom}]"

class GenericTeacher(Person):
    def __init__(self, name, surname, subject):
        Person.__init__(self, name, surname)
        self.subject = subject

    def __str__(self):
        return f"{Person.__str__(self)} {self.subject}"


class Teacher(GenericTeacher):
    def __init__(self, name, surname, classrooms, subject):
        GenericTeacher.__init__(self, name, surname, subject)
        self.classrooms = classrooms

    def __str__(self):
        return f"[Teacher: {GenericTeacher.__str__(self)} {self.classrooms}]"

class Homeroom(GenericTeacher):
    def __init__(self, name, surname, classroom, subject):
        GenericTeacher.__init__(self, name, surname, subject)
        self.classroom = classroom

    def __str__(self):
        return f"[Homeroom teacher: {GenericTeacher.__str__(self)} {self.classroom}]"

'''
Starting functions to use 
'''

def creation_process():

    global students_lst
    global teachers_lst
    global homerooms_lst

    obj = None

    while obj != 4:
        print('---------------- CREATION MENU -------------------\n'
              '1) Student\n'
              '2) Teacher\n'
              '3) Homeroom teacher\n'
              '4) End\n')
        obj = int(input("Please add option: "))


        try:
            if obj == 1:
                print("----------------- Creating Student -------------------------\n\n")
                name = input("Add student name: ")
                surname = input("Add surname: ")
                classroom = input("Add classroom: ")

                student = Student(name, surname, classroom)

                students_lst.append(student)

            elif obj == 2:

                classrooms = []
                print("----------------- Creating Teacher -------------------------\n\n")
                name = input("Add teacher name: ")
                surname = input("Add surname name: ")

                while True:
                    print("\x1B[3m" + "If you want to stop adding teacher classes, press intro" + "\x1B[0m")
                    classroom = input("Add teacher class: ")
                    if classroom == '':
                        break
                    else:
                        classrooms.append(classroom)

                subject = input("Add subject: ")

                teachers = Teacher(name, surname, classrooms, subject)
                teachers_lst.append(teachers)

            elif obj == 3:

                print("----------------- Creating Homeroom teacher -------------------------\n")
                name = input("Add teacher name: ")
                surname = input("Add surname name: ")
                classroom = input("Add classroom: ")
                subject = input("Add subject: ")

                homeroom = Homeroom(name, surname, classroom, subject)
                homerooms_lst.append(homeroom)

            else:
                print("\nPlease add a valid input, please.")

        except ValueError:
            print('\nPlease add string value. \n')
def management_process():
    obj = None
    while obj != 5:
        print('--------------------MANAGEMENT MENU--------------------\n'
              '1) Class\n'
              '2) Student\n'
              '3) Teacher\n'
              '4) Homeroom teacher\n'
              '5) End\n')
        obj = int(input("Please add option: "))

        try:
            if obj == 1:
                cl = None

                print("Displaying all classrooms")
                for i in range(len(students_lst)):
                    print(students_lst[i].classroom)

                cl = input("Please select class to display students and homeroom: ")

                print("List of students for class ", cl)
                for i in range(len(students_lst)):
                    if cl == students_lst[i].classroom:
                        print("- ", students_lst[i].name)

                print("\nTeacher for class", cl)
                for i in range(len(teachers_lst)):
                    classrooms = teachers_lst[i].classrooms
                    for j in range(len(classrooms)):
                        if cl == classrooms[j]:
                            print("- ", teachers_lst[i].name)

            elif obj == 2:
                try:
                    student_name = None
                    student_surname = None

                    print('Lists of classes that a student attend.'
                          '\nPlease add the following information: ')
                    student_name = input("Add student name: ")
                    student_surname = input("Add student surname: ")

                    # Check if student is in records
                    for i in range(len(students_lst)):
                        if student_name != students_lst[i].name and student_surname != students_lst[i].surname:
                            print("This student is not on records")
                        else:
                            print("\nClass attendance: ", students_lst[i].classroom)
                            break
                    # Get teacher
                    for i in range(len(teachers_lst)):
                        classrooms = teachers_lst[i].classrooms
                        for j in range(len(classrooms)):
                            if cl == classrooms[j]:
                                n =  teachers_lst[i].name
                                print("\nTeacher for class", cl, " is ", n)
                            else:
                                print("Not teacher for that class")

                except ValueError:
                    print('\nPlease add string value. \n')

            elif obj == 3:

                teacher_name = None
                teacher_surname = None

                teacher_name = input("Add homeroom name: ")
                teacher_surname = input("Add homeroom surname: ")

                # Check if teacher is in records
                for i in range(len(teachers_lst)):
                    if teacher_name != teachers_lst[i].name and teacher_surname != teachers_lst[i].surname:
                        print("YES"
                              "YES")
                    else:
                        classrooms = teachers_lst[i].classrooms
                        print("- Teacher full name : ", teachers_lst[i].name, " ", teachers_lst[i].surname)
                        print("List of clases: ")
                        for j in range(len(classrooms)):
                            print("- ", classrooms[j])

            elif obj == 4:

                homeroom_name = None
                homeroom_surname = None

                homeroom_name = input("Add homeroom name: ")
                homeroom_surname = input("Add homeroom surname: ")

                # Check if student is in records
                for i in range(len(homerooms_lst)):
                    if homeroom_name != homerooms_lst[i].name and homeroom_surname != homerooms_lst[i].surname:
                        print("YES"
                              "YES")
                    else:
                        cl = homerooms_lst[i].classroom
                        print("- Teacher full name : ", homerooms_lst[i].name, " ", homerooms_lst[i].surname)
                        print("- Subject: ", homerooms_lst[i].subject)
                        print("- Classes: ", homerooms_lst[i].classroom)

                print("\nStundets on that class: \n")
                for i in range(len(students_lst)):
                    if cl == students_lst[i].classroom:
                        print(" - Student full name : ",students_lst[i].name, " ", students_lst[i].surname)


            else:
                print("Return to menu")

        except ValueError:
            print('\nPlease add string value. \n')

def main():
    try:
        op = None
        while op != 3:
            print("--------------------MAIN MENU--------------------\n")
            op = int(input('Select one of the following options: \n'
                       '1) Create\n'
                       '2) Manage\n'
                       '3) end\n'
                       'Add your answer here: '))

            if op == 1:
                creation_process()

            elif op == 2:
                management_process()

            else:
                print('Thanks for using this program!\n')
                exit()

    except ValueError:
        print('\nPlease add correct value. \n')

main()