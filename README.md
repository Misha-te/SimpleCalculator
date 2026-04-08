# SimpleCalculator
Simple Calculator Script

This Python script allows the user to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

# Features
User inputs two numbers.
Choose an operation from a predefined dictionary:
Performs the selected operation and prints the result.
Handles division by zero.
Handles invalid inputs

# How to Use
Run the script in Python.
Enter the first number when prompted.
Enter the second number when prompted.

The script will display the available operations:

These are the operations {'Addition': 1, 'Subs': 2, 'Multiply': 3, 'Division': 4}
Enter the number corresponding to the desired operation.
The result will be printed.
# Example
Please enter the first number: 10
Please enter the second number: 5
These are the operations {'Addition': 1, 'Subs': 2, 'Multiply': 3, 'Division': 4}
Please enter the number of the operation from the dictionary above: 4
Your division is : 2.0

# Error Handling

If the user enters a non-numeric input, the script prints:

    Please enter a valid number

If division by zero is attempted, the script prints:

    Can't divide by Zero

If an invalid operation number is entered, the script prints:

    Please enter valid numbers