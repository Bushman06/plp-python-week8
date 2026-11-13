
# Week 8 Assignment: Final Project — Personal Mini-Toolkit

## Project Description

My Personal Mini-Toolkit is a Python program containing three useful tools:

1. Simple Calculator - Performs addition, subtraction, multiplication, and division.
2. To-Do List - Allows users to add, view, and remove tasks.
3. Number Checker - Checks whether a number is positive, negative, or zero, and whether it is even or odd.

The program uses a repeating menu that allows users to select different tools and return to the main menu until they choose Quit.

## Project Files

- `toolkit_plan.txt` - Contains the project plan, selected tools, menu text, and Python concepts.
- `toolkit.py` - Contains the complete Personal Mini-Toolkit program.
- `screenshots/` - Contains screenshots showing the menu, invalid choice handling, and each tool working.

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run `python toolkit.py`.
5. Select a tool by entering its menu number.

## Reflection

The hardest part of this project was building the menu loop and making sure the program returned to the main menu after each tool finished. The bug that took the longest to fix was handling invalid user input without allowing the program to crash. I learned how to use while loops, if and elif statements, lists, functions, and f-strings in one project. I also learned how to add and remove items from a list while a program is running. Testing each tool helped me understand how different parts of a Python program work together. If I had one more week, I would add a countdown timer and improve the To-Do List so that tasks could be saved in a file and loaded again later.