import csv

def createCsv():

    with open("contacts.csv", "w") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Phone", "Email"])

    print("Contact file created successfully!")


def addContact():

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open("contacts.csv", "a") as file:

        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print(f"Contact added successfully!")

def view():

    with open("contacts.csv", "r") as file:

        read = csv.reader(file)

        for row in read:
            if len(row) == 3:
                print(row[0], row[1], row[2])

def edit():

    view()
    choice = input("Enter the name of the contact you want to modify: ")

    with open("contacts.csv", "r") as file:
            
        contacts = list(csv.reader(file))

    for contact in contacts:
        if len(contact) == 3:
            if contact[0] == choice:

                newPhone = input("Enter new phone number: ")
                newEmail = input("Enter new email address: ")

                if newPhone != "":
                    contact[1] = newPhone
                if newEmail != "":
                    contact[2] = newEmail

                with open("contacts.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerows(contacts)

                return
    
    print("Contact not found")


def main():

    print("Welcome to the Contact Manager App")

    choice = 0

    while choice != 5:
        print("Push the following options to prefore the coresponding action:")
        print("1 - create new contact file")
        print("2 - add new contact")
        print("3 - view all contacts")
        print("4 - modify an existing contact")
        print("5 - save and exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            createCsv()
        elif choice == 2:
            addContact()
        elif choice == 3:
            view()
        elif choice == 4:
            edit()
        elif choice == 5:
            print("Goodbye")

    print("Created by, Teage Blanton")

if __name__ == '__main__':
    main()
