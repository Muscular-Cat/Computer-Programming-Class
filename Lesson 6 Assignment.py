def main():
    student = {}


    student["Jim"] = {
        "ID": 1,
        "GPA": 3.1,
        "Credits": 97,
        "Grades": [80, 50, 100, 98]
    }


    student["Sarah"] = {
        "ID": 2,
        "GPA": 3.6,
        "Credits": 40,
        "Grades": [80, 98]
    }


    print(student)


    print("\nList of students")
    for students in student:
        print(students)


    print("Student Information")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for students in student:
        info = student[students]
        print(f'{students}\t{info["ID"]}\t{info["GPA"]}\t{info["Credits"]}\t\t\t{info["Grades"]}')


    print("\nAccessing student information using the key in a loop")
    for info in student:
        print(info, student[info].items())


    print("\nSarah has dropped out, removing from student info registry")
    student.pop("Sarah")
    print(student)


    print("\nGetting Jim's GPA")
    for name in student:
        print(student[name].get("GPA"))


    print("\nStudents have graduated, clearing the student registry")
    student.clear()
    print(student)


    print("\nCompleted by Teage Blanton - Lesson 6")


if __name__ == "__main__":
    main()
