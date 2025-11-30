import datetime

def addTask(list):
    name = input("Enter the task name:  ")

    date = ""
    
    while True:
        try:
            date = input("Enter the due date (YYYY-MM-DD): ")
            year = date[0:4]
            month = date[5:7]
            day = date[8:]
            date = datetime.date(int(year), int(month), int(day))
            break
        except ValueError:
            print("Format Error: Please try again.")
    
    list.append({"name":name, "date":date})
    print(f"Task '{name}' added with the due date '{date}'.")

def view(list):
    if len(list) == 0:
        print("No tasks to display.")
    else:
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        sunday = monday + datetime.timedelta(days=6)

        print("Tasks due this week: ")

        for task in list:
            if monday <= task["date"] <= sunday:
                print(f" - {task['name']} (Due: {task['date']})")

def listAll(list):
    if len(list) == 0:
        print("No tasks to display.")
    else:
        for task in list:
            print(f"Task: {task['name']}, Date: {task['date']}")

def main():
    print("Welcome to the Weekly Planner App")

    tasks = []
    choice = 0

    while choice != 4:
        print("\n------------------------------")
        print("1 - Add Task")
        print("2 - View Tasks Due This Week")
        print("3 - List All Scheduled Tasks")
        print("4 - Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            addTask(tasks)
        elif choice == 2:
            view(tasks)
        elif choice == 3:
            listAll(tasks)
        elif choice == 4:
            print("Goodbye")
        else:
            print("Not a valid option.")

if __name__ == "__main__":
    main()
