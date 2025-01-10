class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0
if __name__ == "__main__":
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(float, input("Enter the student's grades (separated by space): ").split()))
    student = Student(name, age, grades)
    print("\nStudent Details:")
    student.display_details()
    average = student.calculate_average()
    print(f"Average Grade: {average:.2f}")