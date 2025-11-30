def getInput(prompt1, prompt2):
    mainStr = input(prompt1)
    subStr = input(prompt2)
    return [mainStr, subStr]

def subString(strings):
    if strings[0].find(strings[1]) != -1:
        print(f"\"{strings[1]}\" was found in the main string at index {strings[0].find(strings[1])}.")
    else:
        print(f"\"{strings[1]}\" was not found in the main string.")
    
    return strings[0].find(strings[1])

def question(prompt):
    while True:
        choice = input(prompt)
        if choice == ("y" or "n"):
            return choice
        else:
            print("Error: Not valid option.")

def main():
    print("Welcome to the String Replacment Tool!")
    print("--------------------------------------")

    array = getInput("Enter a string to search through:    ", "Enter a string to search for:    ")
    final = array[0]
    
    print("Searching for substring within the main string, please wait...")
    print("--------------------------------------------------------------")
    i = subString(array)

    if (question(f"Do you want to replace \"{array[1]}\" with something else? (y/n)") == "y"):

        new = input("Enter replacement string:  ")
        
        final = array[0].replace(array[1], new)
    
    print(f"Final String: {final}")

    print("\nThank you for using our program!")

    print("Completed by, Teage Blanton")

if __name__ == "__main__":
    main()
