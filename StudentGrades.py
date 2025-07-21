# Student Grades Manager

# Initialize an empty dictionary to store student grades
student_grades = {}

def add_student():
    name = input("Enter student name: ")
    if name in student_grades:
        print("Student already exists.")
    else:
        grade = input("Enter grade for " + name + ": ")
        student_grades[name] = grade
        print("Student added successfully.")

def update_grade():
    name = input("Enter student name to update: ")
    if name in student_grades:
        grade = input("Enter new grade for " + name + ": ")
        student_grades[name] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def print_all_grades():
    if not student_grades:
        print("No students found.")
    else:
        print("\n--- Student Grades ---")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
        print("----------------------")

# Main menu loop
while True:
    print("\nStudent Grades Menu:")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        print_all_grades()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
