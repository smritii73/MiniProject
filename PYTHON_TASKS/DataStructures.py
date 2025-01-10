def add_student(students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = list(map(float, input("Enter student's grades (separated by space): ").split()))
    students[name] = {"age": age, "grades": grades}
    print(f"Student {name} added successfully!")

def view_students(students):
    if not students: print("No students.")
    else:
        for name, data in students.items():
            print(f"Name: {name}, Age: {data['age']}, Grades: {data['grades']}")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    if name in students:
        age = int(input(f"Enter new age for {name} (current: {students[name]['age']}): "))
        grades = list(map(float, input("Enter new grades (separated by space): ").split()))
        students[name] = {"age": age, "grades": grades}
        print(f"Student {name} updated successfully!")
    else:
        print(f"Student {name} not found.")

def delete_student(students):
    name = input("Enter the name of the student to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully!")
    else: print(f"Student {name} not found.")
def main():
    students = {}
    while True:
        print("\nStudent Data Management:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit") 
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()