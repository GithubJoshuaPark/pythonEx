# lessons/lesson16.py
import os
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates exception handling using try, except, else, and finally blocks.
    """
    print("--- Lesson 16: Exceptions (try, except, finally) ---")

    # 1. Basic try-except block
    # Used to catch and handle errors (exceptions) that occur during execution.
    print("\n--- Basic try-except ---")
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    print("Program continues after handling the error.")
    print("-" * 20)

    # 2. Catching specific exceptions
    # It's good practice to catch specific exceptions rather than a general one.
    print("\n--- Catching specific exceptions ---")
    try:
        value = int("hello") # This will raise a ValueError
    except ValueError:
        print("Error: Invalid conversion from string to integer.")

    try:
        my_list = [1, 2]
        print(my_list[3]) # This will raise an IndexError
    except IndexError:
        print("Error: List index out of range.")
    print("-" * 20)

    # 3. Catching multiple exceptions in one except block
    print("\n--- Catching multiple exceptions ---")
    try:
        # Example 1: IndexError
        # x = [1, 2][5]
        # Example 2: ValueError
        x = int("abc")
    except (IndexError, ValueError) as e:
        print(f"Caught an error: {e}")
    print("-" * 20)

    # 4. Catching a general exception (less specific, use with caution)
    # This will catch any type of exception.
    print("\n--- Catching a general exception ---")
    try:
        # result = 1 / 0
        another_value = "Python" + 1 # This will raise a TypeError
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 20)

    # 5. The try-except-else block
    # The 'else' block executes only if the 'try' block completes without any exceptions.
    print("\n--- try-except-else block ---")
    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
        else:
            print("Division successful.")
            return result

    print(f"Dividing 10 by 2: {safe_divide(10, 2)}")
    print(f"Dividing 10 by 0: {safe_divide(10, 0)}")
    print("-" * 20)

    # 6. The try-except-finally block
    # The 'finally' block always executes, regardless of whether an exception occurred or not.
    # It's typically used for cleanup operations (e.g., closing files).
    print("\n--- try-except-finally block ---")
    def process_file(filename):
        file = None # Initialize file to None
        try:
            file = open(filename, 'r')
            content = file.read()
            print(f"File content: {content[:20]}...")
            # Simulate an error
            # 1 / 0
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred during file processing: {e}")
        finally:
            if file: # Check if file object was successfully created
                file.close()
                print(f"File '{filename}' closed in finally block.")

    # Create a temporary file for demonstration
    temp_file = "temp_lesson16.txt"
    with open(temp_file, 'w') as f:
        f.write("This is a temporary file for exception handling.")

    process_file(temp_file)
    print("\n--- Testing with non-existent file ---")
    process_file("non_existent_file.txt")

    # Clean up the temporary file
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print("-" * 20)

    # 7. Raising Exceptions
    # You can explicitly raise an exception using the 'raise' keyword.
    print("\n--- Raising exceptions ---")
    def validate_age(age):
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a number.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print(f"Age {age} is valid.")

    try:
        validate_age(-5)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        validate_age("twenty")
    except TypeError as e:
        print(f"Caught expected error: {e}")

    validate_age(25)
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)