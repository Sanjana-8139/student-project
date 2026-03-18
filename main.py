from student_manager import StudentManager

manager = StudentManager()

while True:
    print("\nStudent Management system")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        name = input("Enter the name of the student:")
        roll = int(input("Enter the roll of te student:"))
        marks = float(input("Enter the marks of the student:"))
        age = int(input("Enter the age of the student:"))
        manager.add_student(name,roll,marks,age)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":

        roll = int(input("Enter Roll to search: "))
        manager.search_student(roll)

    elif choice == "4":

        roll = int(input("Enter Roll to update: "))
        manager.update_student(roll)

    elif choice == "5":

        roll = int(input("Enter Roll to delete: "))
        manager.delete_student(roll)

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("invalid Choice:")

    