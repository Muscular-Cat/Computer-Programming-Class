import random


def main():
    grades = []
    while True:
        grade = int(input("Please enter a grade or -1 to stop: "))
        if grade == -1:
            break
        else:
            grades.append(grade)
    print(grades)
    print("Reoving lowest grade")
    grades.pop(grades.index(min(grades)))
    print(grades)
    print("Removing random grade")
    grades.remove(random.choice(grades))
    print(grades)
    print("Edit a grade")
    x = 1
    for num in grades:
        print(f"{x}. {num}")
        x+=1
    choice = int(input("Which grade do you want to edit: "))
    print("Please enter a valid grade!")
    while choice < 1 or choice > len(grades):
            choice = int(input(f"Which grade do you want to edit (enter a number 1 through {len(grades)}): "))
    grades[choice-1] = int(input("Enter the new grade: "))
    print(grades)
    print("Sorting and reversing list")
    grades.sort()
    grades.reverse()
    print("Getting grade total and average")
    print(f"Total: {sum(grades)}")
    print(f"Average: {(sum(grades)/len(grades))}")
    print("Completed by, Teage Blanton")


if __name__ == "__main__":
    main()
