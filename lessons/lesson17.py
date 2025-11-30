# lessons/lesson17.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates how to create custom exceptions and best practices for error design.
    """
    print("--- Lesson 17: Custom Exceptions and Error Design ---")

    # 1. Why Custom Exceptions?
    # - Improve code readability and clarity.
    # - Provide more specific error messages for debugging and user feedback.
    # - Allow for more granular error handling.
    # - Encapsulate error-related information.

    # 2. Defining a Custom Exception
    # Custom exceptions should inherit from Python's built-in 'Exception' class
    # or a more specific built-in exception (e.g., ValueError, TypeError).

    class InvalidInputError(Exception):
        """Custom exception raised when an invalid input is provided."""
        def __init__(self, message="Invalid input provided", value=None):
            self.message = message
            self.value = value
            super().__init__(self.message)

        def __str__(self):
            if self.value is not None:
                return f"{self.message}: '{self.value}'"
            return self.message

    class NegativeValueError(ValueError):
        """Custom exception raised when a negative value is encountered where it's not allowed."""
        def __init__(self, message="Negative value is not allowed", value=None):
            self.message = message
            self.value = value
            super().__init__(self.message)

        def __str__(self):
            if self.value is not None:
                return f"{self.message}: {self.value}"
            return self.message

    print("\n--- Custom Exception Definitions ---")
    print("Defined InvalidInputError and NegativeValueError.")
    print("-" * 20)

    # 3. Raising and Handling Custom Exceptions

    def process_data(data):
        """Processes data, raising custom exceptions for invalid cases."""
        if not isinstance(data, (int, float)):
            raise InvalidInputError("Data must be a number", value=data)
        if data < 0:
            raise NegativeValueError(value=data)
        if data > 100:
            raise InvalidInputError("Data value too high", value=data)
        return data * 2

    print("\n--- Raising and Handling Custom Exceptions ---")
    # Test case 1: Valid input
    try:
        result = process_data(50)
        print(f"Processed data (50): {result}")
    except (InvalidInputError, NegativeValueError) as e:
        print(f"Caught exception: {e}")

    # Test case 2: Invalid type
    try:
        process_data("abc")
    except InvalidInputError as e:
        print(f"Caught InvalidInputError: {e}")
    except NegativeValueError as e: # This won't be caught here
        print(f"Caught NegativeValueError (unexpected): {e}")

    # Test case 3: Negative value
    try:
        process_data(-10)
    except NegativeValueError as e:
        print(f"Caught NegativeValueError: {e}")
    except InvalidInputError as e: # This won't be caught here
        print(f"Caught InvalidInputError (unexpected): {e}")

    # Test case 4: Value too high
    try:
        process_data(150)
    except InvalidInputError as e:
        print(f"Caught InvalidInputError: {e}")
    print("-" * 20)

    # 4. Error Design Best Practices

    # a) When to use exceptions vs. returning error codes/None
    #    - Exceptions for truly exceptional, unexpected, or unrecoverable conditions.
    #    - Return codes/None for expected outcomes, often for flow control.

    # Example: Function returning None for expected 'not found'
    def find_item(item_list, item):
        """Returns item index if found, None otherwise."""
        try:
            return item_list.index(item)
        except ValueError:
            return None

    my_items = ["apple", "banana", "cherry"]
    print(f"\n--- Error Design: Return None for expected 'not found' ---")
    index = find_item(my_items, "banana")
    if index is not None:
        print(f"Banana found at index: {index}")
    else:
        print("Banana not found.")

    index = find_item(my_items, "grape")
    if index is not None:
        print(f"Grape found at index: {index}")
    else:
        print("Grape not found.")
    print("-" * 20)

    # b) Making exceptions specific
    #    - Don't just raise generic 'Exception'.
    #    - Use or inherit from specific built-in exceptions where appropriate.
    #    - Custom exceptions add domain-specific meaning.

    # c) Logging exceptions (instead of just printing)
    #    - In real-world applications, exceptions are often logged using the 'logging' module.
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    def divide_numbers_logged(a, b):
        try:
            result = a / b
            logging.info(f"Division successful: {a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            logging.error("Attempted to divide by zero!")
            # Optionally re-raise or return a default value
            return None
        except TypeError as e:
            logging.critical(f"Type error during division: {e}")
            raise # Re-raise if this error is critical and cannot be handled locally

    print("\n--- Error Design: Logging Exceptions ---")
    divide_numbers_logged(10, 2)
    divide_numbers_logged(10, 0)
    try:
        divide_numbers_logged("10", 2)
    except TypeError:
        print("Caught re-raised TypeError.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)