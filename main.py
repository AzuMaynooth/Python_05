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
        super().__init__(name, surname)
        self.classroom = classroom

    def __str__(self):
        return f"[Student: {super().__str__()} {self.classroom}]"

class GenericTeacher(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} {self.subject}"

class Teacher(GenericTeacher):
    def __init__(self, name, surname, classrooms, subject):
        super().__init__(name, surname, subject)
        self.classrooms = classrooms

    def __str__(self):
        return f"[Teacher: {super().__str__()} {self.classrooms}]"

class Homeroom(GenericTeacher):
    def __init__(self, name, surname, classroom, subject):
        super().__init__(name, surname, subject)
        self.classroom = classroom

    def __str__(self):
        return f"[Homeroom teacher: {super().__str__()} {self.classroom}]"

def create_user():
    while True:
        print("\n--- User Creation Menu ---")
        print("Options: student, teacher, homeroom teacher, end")
        user_type = input("Enter the type of user to create: ").strip().lower()

        if user_type == "student":
            name = input("Enter student's first name: ")
            surname = input("Enter student's last name: ")
            classroom = input("Enter student's classroom (e.g., 3C): ")
            student = Student(name, surname, classroom)
            students_lst.append(student)
            print(f"Student {name} {surname} added to class {classroom}.")

        elif user_type == "teacher":
            name = input("Enter teacher's first name: ")
            surname = input("Enter teacher's last name: ")
            subject = input("Enter teacher's subject: ")
            classrooms = []
            print("Enter the classes the teacher teaches (press Enter to stop):")
            while True:
                classroom = input("Classroom: ").strip()
                if classroom == "":
                    break
                classrooms.append(classroom)
            teacher = Teacher(name, surname, classrooms, subject)
            teachers_lst.append(teacher)
            print(f"Teacher {name} {surname} added, teaches {subject} in {classrooms}.")

        elif user_type == "homeroom teacher":
            name = input("Enter homeroom teacher's first name: ")
            surname = input("Enter homeroom teacher's last name: ")
            classroom = input("Enter the homeroom teacher's class: ")
            subject = input("Enter homeroom teacher's subject: ")
            homeroom = Homeroom(name, surname, classroom, subject)
            homerooms_lst.append(homeroom)
            print(f"Homeroom teacher {name} {surname} added for class {classroom}.")

        elif user_type == "end":
            print("Returning to main menu.")
            break

        else:
            print("Invalid option. Please try again.")

def manage_user():
    while True:
        print("\n--- User Management Menu ---")
        print("Options: class, student, teacher, homeroom teacher, end")
        action = input("Enter the option to manage: ").strip().lower()

        if action == "class":
            classroom = input("Enter the classroom to view (e.g., 3C): ").strip()
            print(f"\nStudents in class {classroom}:")
            for student in students_lst:
                if student.classroom == classroom:
                    print(f"- {student.name} {student.surname}")
            print(f"\nHomeroom teacher for class {classroom}:")
            for homeroom in homerooms_lst:
                if homeroom.classroom == classroom:
                    print(f"- {homeroom.name} {homeroom.surname} ({homeroom.subject})")

        elif action == "student":
            name = input("Enter student's first name: ").strip()
            surname = input("Enter student's last name: ").strip()
            found = False
            for student in students_lst:
                if student.name == name and student.surname == surname:
                    found = True
                    print(f"\n{student.name} {student.surname} attends class {student.classroom}.")
                    for teacher in teachers_lst:
                        if student.classroom in teacher.classrooms:
                            print(f"- Taught by {teacher.name} {teacher.surname} ({teacher.subject}).")
                    break
            if not found:
                print("Student not found.")

        elif action == "teacher":
            name = input("Enter teacher's first name: ").strip()
            surname = input("Enter teacher's last name: ").strip()
            found = False
            for teacher in teachers_lst:
                if teacher.name == name and teacher.surname == surname:
                    found = True
                    print(f"\n{teacher.name} {teacher.surname} teaches {teacher.subject} in: {', '.join(teacher.classrooms)}.")
                    break
            if not found:
                print("Teacher not found.")

        elif action == "homeroom teacher":
            name = input("Enter homeroom teacher's first name: ").strip()
            surname = input("Enter homeroom teacher's last name: ").strip()
            found = False
            for homeroom in homerooms_lst:
                if homeroom.name == name and homeroom.surname == surname:
                    found = True
                    print(f"\nHomeroom teacher {homeroom.name} {homeroom.surname} leads class {homeroom.classroom}.")
                    print(f"Subject: {homeroom.subject}")
                    print("\nStudents:")
                    for student in students_lst:
                        if student.classroom == homeroom.classroom:
                            print(f"- {student.name} {student.surname}")
                    break
            if not found:
                print("Homeroom teacher not found.")

        elif action == "end":
            print("Returning to main menu.")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\n--- Main Menu ---")
        print("Options: create, manage, end")
        command = input("Enter a command: ").strip().lower()

        if command == "create":
            create_user()

        elif command == "manage":
            manage_user()

        elif command == "end":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

main()
