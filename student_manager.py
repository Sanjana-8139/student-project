import json
from student import Student

class StudentManager:

    def __init__(self):
        self.students = []
        self.load_students()

    def add_student(self,name,roll,marks,age):
        student = Student(name,roll,marks,age)
        self.students.append(student)
        self.save_students()
        print("Student added successfully !")

    def display_students(self):

        if len(self.students) == 0:
            print("No students found")
            return
    
        for s in self.students:
            print(f" Name :{s.name},Roll:{s.roll},Marks:{s.marks},Age :{s.age}")

    def search_student(self,roll):

        for s in self.students:
            if s.roll == roll:
                print(f" Name :{s.name},Roll:{s.roll},Marks:{s.marks},Age :{s.age}")
                return
        print("Student Not Found")

    def update_student(self,roll):

        for s in self.students:
            if s.roll == roll:
                s.name = input("Enter the name:")
                s.marks = float(input("enter the marks of the student:"))
                s.age = int(input("Enter the age of the student:"))
                self.save_students()
                print("Student updated successfully!")
                return
        print("Student not found:")

    def delete_student(self, roll):

        for s in self.students:

            if s.roll == roll:
               self.students.remove(s)
               self.save_students()
               print("Student deleted successfully!")
               return

        print("Student not found")
    
    def load_students(self):
        try:
            with open("students.json","r") as file:

                data = json.load(file)

                for item in data:
                    student = Student.from_dict(item)
                    self.students.append(student)

        except FileNotFoundError:
           pass

    def save_students(self):

       data = []

       for s in self.students:
           data.append(s.to_dict())

       with open("students.json","w") as file:
         json.dump(data,file,indent=4)