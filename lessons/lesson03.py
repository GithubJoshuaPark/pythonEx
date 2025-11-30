# lessons/lesson03.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates basic input and output operations in Python.
    """
    print("--- Lesson 03: Basic Input/Output ---")

    # 1. Output using print()
    # The print() function is used to output messages to the console.

    # Basic print statement
    print("Hello from Lesson 03!")

    # Printing multiple items (separated by a space by default)
    print("My favorite number is", 7)

    # Using 'sep' (separator) argument
    print("apple", "banana", "cherry", sep=", ")

    # Using 'end' argument (what to print at the end, default is newline)
    print("This is on the same line.", end=" ")
    print("Continuing here.")

    # Formatted output using f-strings (formatted string literals)
    name = "Python"
    version = 3.9
    print(f"Welcome to {name} programming, version {version:.1f}!")
    print("-" * 20)

    # 2. Input using input()
    # The input() function is used to get input from the user.
    # It always returns the input as a string.

    # Getting a string input
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}!")

    # Getting a numerical input and converting it
    # Remember: input() always returns a string, so you often need to convert it.
    try:
        age_str = input("Please enter your age: ")
        user_age = int(age_str) # Convert string to integer
        print(f"You are {user_age} years old.")
        print(f"In 5 years, you will be {user_age + 5}.")
    except ValueError:
        print("Invalid age entered. Please enter a number.")

    # Getting a float input
    try:
        height_str = input("Please enter your height in meters (e.g., 1.75): ")
        user_height = float(height_str) # Convert string to float
        print(f"Your height is {user_height} meters.")
    except ValueError:
        print("Invalid height entered. Please enter a number.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)