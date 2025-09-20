first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
current_year = int(input("Enter the current year:"))
birth_year = int(input("Enter your birth year:"))
age = current_year - birth_year

print("Hello", first_name, last_name, "!\n"\
    "You are", str(age), "years old this year.\n\n"\
    "In the next year", str(current_year+1), ", you will be", str(age+1), "years old.")
