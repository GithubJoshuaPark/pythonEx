# lessons/lesson22.py
import logging
import os
import sys
import utils

utils.show_base_name(__file__, True)

# Define a log file path (relative to where the script is run)
LOG_FILE = "lesson22.log"

def setup_logging():
    """Configures the logging system for console and file output."""
    # Ensure the log file is clean for each run of the lesson
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # Set the lowest level to capture everything

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(LOG_FILE)

    # Set levels for handlers (optional, but useful for different outputs)
    console_handler.setLevel(logging.INFO) # Only INFO and above to console
    file_handler.setLevel(logging.DEBUG)  # All DEBUG and above to file

    # Create formatters and add them to handlers
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Get the logger for this module
logger = setup_logging()

def divide(a, b):
    """Performs division and logs the process."""
    logger.debug(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Error: Attempted to divide by zero!")
        return None
    except TypeError:
        logger.warning(f"Warning: Division operands {a}, {b} should be numeric.")
        logger.exception("TypeError occurred during division.") # Logs traceback
        return None

def main():
    """
    This lesson demonstrates basic logging and debugging techniques in Python.
    """
    print("--- Lesson 22: Logging and Debugging Basics ---")

    # 1. Why Logging?
    # Logging is a powerful way to track events that happen when some
    # software runs. Developers use it to understand the flow of control
    # and to pinpoint problems. It's often better than print statements
    # for production code because:
    # - You can control message levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    # - You can send logs to different destinations (console, file, network).
    # - It's easy to include timestamps, module names, etc.

    print("\n--- 1. Logging: See console output and check 'lesson22.log' file ---")
    logger.debug("This is a DEBUG message. (Only in file)")
    logger.info("This is an INFO message. (Console and file)")
    logger.warning("This is a WARNING message. (Console and file)")
    logger.error("This is an ERROR message. (Console and file)")
    logger.critical("This is a CRITICAL message. (Console and file)")
    print("-" * 20)

    # 2. Using Logging in a Function
    print("\n--- 2. Logging in a function ---")
    divide(10, 2)
    divide(10, 0)
    divide("hello", 5) # This will cause a TypeError and be logged
    print("-" * 20)

    # 3. Basic Debugging Techniques

    # a) Using print statements (simple but can be messy in large codebases)
    print("\n--- 3a. Debugging with print() (for quick checks) ---")
    def calculate_sum(numbers):
        total = 0
        print(f"DEBUG: Initial total = {total}") # Debug print
        for num in numbers:
            total += num
            print(f"DEBUG: Added {num}, current total = {total}") # Debug print
        return total

    my_numbers = [1, 2, 3]
    result_sum = calculate_sum(my_numbers)
    print(f"Result of calculate_sum: {result_sum}")
    print("-" * 20)

    # b) Using assertions
    # An assertion is a sanity check that you can turn on or turn off when you have finished debugging.
    # It checks if a condition is true, and if not, it raises an AssertionError.
    print("\n--- 3b. Debugging with assert statements ---")
    def apply_discount(price, discount_percentage):
        assert 0 <= discount_percentage <= 100, "Discount percentage must be between 0 and 100."
        final_price = price * (1 - discount_percentage / 100)
        return final_price

    try:
        print(f"Price after 10% discount: {apply_discount(100, 10)}")
        print(f"Price after 50% discount: {apply_discount(200, 50)}")
        # This will raise an AssertionError
        # print(f"Price after 110% discount: {apply_discount(50, 110)}")
    except AssertionError as e:
        print(f"Caught assertion error: {e}")
    print("-" * 20)

    # c) Using Python's built-in debugger (pdb)
    # For more interactive debugging, you can use pdb.
    # To use it, you can insert 'breakpoint()' (Python 3.7+) or 'import pdb; pdb.set_trace()'
    # where you want to start debugging.
    # When execution hits that line, it will drop you into a console where you can:
    # - 'n' (next): execute the next line of code.
    # - 's' (step): step into a function call.
    # - 'c' (continue): continue execution until the next breakpoint or program end.
    # - 'p variable_name': print the value of a variable.
    # - 'q' (quit): exit the debugger.

    print("\n--- 3c. Debugging with pdb ---")
    print("To demonstrate pdb, uncomment 'breakpoint()' in the code and run this lesson.")
    print("When in pdb, type 'n' to go next, 'c' to continue, 'p variable_name' to inspect.")

    def debugger_example(a, b):
        intermediate_result = a + b
        # uncomment the line below to activate the debugger
        # breakpoint() # Python 3.7+
        final_result = intermediate_result * 2
        return final_result

    # If you uncommented breakpoint(), run:
    # python lessons/lesson22.py
    # Then type 'n', 'p intermediate_result', 'n', 'p final_result', 'c'
    # Or 's' to step into functions

    # debugger_example(10, 5)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
    # Shut down the logging system to release file handlers
    logging.shutdown()
    # Clean up the log file at the end of the lesson
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
else:
    utils.show_base_name(__file__, False)