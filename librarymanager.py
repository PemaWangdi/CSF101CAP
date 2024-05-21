students_list = []
students_dict = {}

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    students_list.append(name)
    students_dict[name] = {"age": age, "grade": grade}
    
    print("Student information added successfully.")

def view_students():
    print("Student Details:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

def search_student(name):
    if name in students_dict:
        info = students_dict[name]
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("Student not found.")

def remove_student(name):
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

# Test the system
add_student()
add_student()
view_students()
search_student("Alice")
remove_student("Bob")
view_students()
