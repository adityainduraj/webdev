class Student:
    def __init__(self, name, roll_no, department, address, gender, marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.address = address
        self.gender = gender
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = self.total_marks / len(marks)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Department: {self.department}")
        print(f"Address: {self.address}")
        print(f"Gender: {self.gender}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Percentage: {self.percentage:.2f}%")

def main():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        department = input("Enter department: ")
        address = input("Enter address: ")
        gender = input("Enter gender: ")
        marks = [int(input(f"Enter marks for subject {_+1}: ")) for _ in range(3)]
        students.append(Student(name, roll_no, department, address, gender, marks))
        print("\n")
    for student in students:
        student.display_details()
        print()
    max_marks_student = max(students, key=lambda s: s.total_marks)
    min_marks_student = min(students, key=lambda s: s.total_marks)
    fail_students = [student for student in students if any(mark < 10 for mark in student.marks)]
    print(f"Student with maximum marks: {max_marks_student.name}")
    print(f"Student with minimum marks: {min_marks_student.name}")
    if fail_students:
        print("Students who failed:")
        for student in fail_students:
            print(student.name)
    else:
        print("No students failed.")

if __name__ == "__main__":
    main()
