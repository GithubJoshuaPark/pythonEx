# lessons/lesson14.py

# It's good practice to put imports at the top of the file
import math
import random
import os
import sys
import datetime

# You can also import specific items from a module
from collections import Counter

# Importing a local module (e.g., utils.py)
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates modules, import statements, and Python's Standard Library.
    """
    print("--- Lesson 14: Modules, Imports, and Standard Library ---")

    # 1. What is a Module?
    # A module is a file containing Python definitions and statements.
    # The file name is the module name with the suffix .py appended.
    # Modules are used to organize code into logical units.

    # 2. Importing Modules
    # We use the 'import' statement to bring modules into our current scope.

    print("\n--- Basic Import Examples ---")
    # Using 'math' module (we imported it at the top)
    print(f"Value of pi from math module: {math.pi}")
    print(f"Square root of 16 from math module: {math.sqrt(16)}")

    # Using 'random' module
    print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
    print(f"Random choice from a list: {random.choice(['rock', 'paper', 'scissors'])}")
    print("-" * 20)

    # 3. Different Ways to Import

    # a) import module_name as alias
    # Gives the module a shorter or different name.
    import datetime as dt
    current_time = dt.datetime.now()
    print(f"Current date and time (using alias dt): {current_time}")

    # b) from module_name import specific_item
    # Imports only specific attributes or functions, so you don't need module_name. prefix.
    # We imported 'Counter' from 'collections' this way.
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_counts = Counter(words)
    print(f"Word counts using Counter: {word_counts}")

    # c) from module_name import item1, item2 as alias2
    from os import path as os_path
    print(f"Current working directory (using os_path): {os_path.abspath('.')}")

    # d) from module_name import * (Generally discouraged)
    # Imports all public names from the module. Can lead to name clashes.
    # Example (don't do this in large projects):
    # from math import *
    # print(sqrt(25)) # No 'math.' prefix needed
    print("-" * 20)

    # 4. Python Standard Library
    # A collection of script modules that are automatically available to Python programs.

    print("\n--- Examples from Standard Library ---")

    # os module: Interacting with the operating system
    print(f"Current working directory: {os.getcwd()}")
    # os.mkdir("test_dir") # Uncomment to create a directory
    # print(f"List files in current directory: {os.listdir('.')}")
    # os.rmdir("test_dir") # Uncomment to remove a directory

    # sys module: System-specific parameters and functions
    print(f"Python version: {sys.version}")
    print(f"Python executable path: {sys.executable}")
    print(f"Module search path (sys.path): {sys.path[:3]}...") # Show first 3 entries

    # datetime module: Working with dates and times
    today = datetime.date.today()
    print(f"Today's date: {today}")
    now = datetime.datetime.now()
    print(f"Current datetime: {now}")
    print(f"Formatted datetime: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 20)

    # 5. Local Modules
    # You can create your own modules. We have 'utils.py' in this project.
    print("\n--- Using a local module (utils.py) ---")
    print(f"Greeting from utils: {utils.greet('Learner')}")
    print(f"Random emojis from utils: {utils.get_random_emojis(2)}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)