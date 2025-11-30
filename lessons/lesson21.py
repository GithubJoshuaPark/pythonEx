# lessons/lesson21.py
import sys
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates how to handle command-line arguments using sys.argv.
    """
    print("--- Lesson 21: Command Line Arguments with sys.argv ---")

    # 1. What are Command Line Arguments?
    # Command-line arguments are additional pieces of information passed to a
    # Python script when it is executed from the command line.
    # They allow you to customize the script's behavior without modifying its code.

    # 2. The sys.argv List
    # The 'sys' module provides access to system-specific parameters and functions.
    # 'sys.argv' is a list in Python that contains the command-line arguments.
    # - sys.argv[0] is always the name of the script itself.
    # - sys.argv[1] is the first argument, sys.argv[2] the second, and so on.

    print(f"\n--- sys.argv content ---")
    print(f"sys.argv list: {sys.argv}")
    print(f"Number of arguments: {len(sys.argv)}")
    print("-" * 20)

    # 3. Accessing Individual Arguments
    # We can access arguments by their index.
    print(f"\n--- Accessing individual arguments ---")
    if len(sys.argv) > 0:
        print(f"Script name (sys.argv[0]): '{sys.argv[0]}'")
    if len(sys.argv) > 1:
        print(f"First argument (sys.argv[1]): '{sys.argv[1]}'")
    if len(sys.argv) > 2:
        print(f"Second argument (sys.argv[2]): '{sys.argv[2]}'")
    print("-" * 20)

    # To run this example from your terminal:
    # python lessons/lesson21.py hello world 123

    # 4. Converting Arguments to Other Types
    # Command-line arguments are always strings. If you expect numbers,
    # you need to convert them.

    print(f"\n--- Converting arguments to other types ---")
    if len(sys.argv) > 2:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            sum_nums = num1 + num2
            print(f"Arguments as integers: {num1} + {num2} = {sum_nums}")
        except ValueError:
            print(f"Error: Could not convert '{sys.argv[1]}' or '{sys.argv[2]}' to integers.")
    else:
        print("Please provide at least two numbers as arguments to see conversion example.")
    print("-" * 20)

    # To run this example:
    # python lessons/lesson21.py 10 20
    # python lessons/lesson21.py apple banana

    # 5. Handling Missing Arguments
    # It's important to check if the required number of arguments are provided.

    print(f"\n--- Handling missing arguments ---")
    if len(sys.argv) < 2:
        print("Usage: python lessons/lesson21.py <your_name>")
    else:
        user_name = sys.argv[1]
        print(f"Hello, {user_name}!")
    print("-" * 20)

    # 6. Example: Simple Calculator
    print(f"\n--- Example: Simple Calculator ---")
    if len(sys.argv) == 4:
        operation = sys.argv[1]
        try:
            operand1 = float(sys.argv[2])
            operand2 = float(sys.argv[3])

            if operation == "add":
                print(f"{operand1} + {operand2} = {operand1 + operand2}")
            elif operation == "subtract":
                print(f"{operand1} - {operand2} = {operand1 - operand2}")
            elif operation == "multiply":
                print(f"{operand1} * {operand2} = {operand1 * operand2}")
            elif operation == "divide":
                if operand2 != 0:
                    print(f"{operand1} / {operand2} = {operand1 / operand2}")
                else:
                    print("Error: Cannot divide by zero.")
            else:
                print(f"Invalid operation: '{operation}'. Use add, subtract, multiply, or divide.")
        except ValueError:
            print("Error: Operands must be valid numbers.")
    else:
        print("Usage for calculator: python lessons/lesson21.py <operation> <number1> <number2>")
        print("  Example: python lessons/lesson21.py add 5 3")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)