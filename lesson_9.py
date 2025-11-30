def main():
    
    print("Welcome to the Simple Buget Tracker")
    print("-------------------------------------")

    income = 0

    while income <= 0:
        try:
            income = float(input("Enter your total income:  "))

            if income < 0:
                print("Income cannot be negative...")
        
        except ValueError as e:
            print("Error:", e, ". Plesse enter valid ammount.")

    expenses = []

    while True:

        try:
            expense = float(input("Enter an expense amount (or 0 to exit):  "))

            if expense == 0:
                break
            elif expense < 0:
                print("Expense cannot be negative...")
            else:
                expenses.append(expense)

        except ValueError as e:
            print("Error:", e, ". Plesse enter valid ammount.")

    total = sum(expenses)

    print("Budget Results")
    print("----------------")

    print(f"Total Income:  ${income:,.2f}")
    print(f"Total Expenses: ${total:,.2f}")
    print(f"Remaining Budget: ${(income - total):,.2f}")

    print("Complete Expense List")
    print("-----------------------")

    for num in expenses:
        print(f"${(num):,.2f}")

    print("Completed by, Teage Blanton")
if __name__ == "__main__":
    main()