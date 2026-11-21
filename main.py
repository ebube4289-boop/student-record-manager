import json
def add_student(name, age, score):
    student = {
        "name": name,
        "age": age,
        "score": score
    }    
    return student

def view_students(students):
    if not students:
        print("no students found.")
    for student in students:
        print(student["name"])
        print(student["age"])
        print(student["score"])


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None

def delete_student(students, name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            return True

    return False

def update_score(students, name, new_score):
    for student in students:
        if student["name"] == name:
            student["score"] = new_score
            return True
    return False

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        return students
    except FileNotFoundError:
        return []
students = load_students()

while True:
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update score")
    print("5. Delete student")
    print("6. Exit")
    choice = input("choose an option: ")
    if choice == "6":
        print("goodbye")
        break
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        name = input("Enter student name to search: ")
        student = find_student(students, name)

        if student is None:
            print("student not found")
        else:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Score:", student["score"])
    elif choice == "4":
        name = input("enter student name: ")
        new_score = int(input("enter new score"))

        if update_score(students, name, new_score):
            save_students(students)
            print("score updated successfully")
        else:
            print("student not found")
    elif choice == "5":
        name = input("enter student name to be deleted: ")
        if delete_student(students, name):
            save_students(students)
            print("student successfully deleted")
        else:
            print("student not found")
    elif choice == "1":
        name = input("enter student name: ")
        age = int(input("enter student age: "))
        score = int(input("enter student score: "))

        student = add_student(name, age, score)
        students.append(student)
        save_students(students)

        print("student added successfully")