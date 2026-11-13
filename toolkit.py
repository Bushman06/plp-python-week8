# Personal Mini-Toolkit - Week 8 Final Project


# Helper function: Get a valid number from the user
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


# TOOL 1: Simple Calculator
# This tool performs addition, subtraction, multiplication, and division.
def calculator():
    print("\n--- Simple Calculator ---")

    first = get_number("Enter the first number: ")
    second = get_number("Enter the second number: ")

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter your choice (1-4): ")

    if operation == "1":
        result = first + second
        print(f"Result: {first} + {second} = {result}")

    elif operation == "2":
        result = first - second
        print(f"Result: {first} - {second} = {result}")

    elif operation == "3":
        result = first * second
        print(f"Result: {first} * {second} = {result}")

    elif operation == "4":
        if second == 0:
            print("Sorry, you cannot divide by zero.")
        else:
            result = first / second
            print(f"Result: {first} / {second} = {result}")

    else:
        print("Invalid operation. Please choose from 1 to 4.")


# TOOL 2: To-Do List
# This tool allows users to add, view, and remove tasks from a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


# TOOL 3: Number Checker
# This tool checks whether a number is positive, negative, or zero,
# and whether it is even or odd.
def number_checker():
    print("\n--- Number Checker ---")

    number = get_number("Enter a whole number: ")

    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("The number is zero.")

    if number.is_integer():
        if int(number) % 2 == 0:
            print(f"{int(number)} is an even number.")
        else:
            print(f"{int(number)} is an odd number.")
    else:
        print("Even or odd applies to whole numbers, not decimals.")


# MAIN PROGRAM: Display the menu until the user chooses Quit.
print("===================================")
print("Welcome to My Personal Mini-Toolkit!")
print("===================================")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        number_checker()

    elif choice == "4":
        print("\nThank you for using My Personal Mini-Toolkit!")
        print("Goodbye!")

        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
