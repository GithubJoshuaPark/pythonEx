# lessons/lesson02.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates variables and common data types in Python.
    """
    print("--- Lesson 02: Variables and Data Types ---")

    # 1. Variables
    # A variable is a container for storing a value. Python is dynamically typed,
    # so you don't need to declare the type of a variable.
    message = "Hello, Python learners!"
    print(f"Variable 'message': {message}")

    # You can change the value and even the type of a variable.
    x = 100
    print(f"x is initially: {x} (type: {type(x)})")
    x = "Now I'm a string!"
    print(f"x is now: {x} (type: {type(x)})")
    print("-" * 20)

    # 2. Common Data Types

    # a) Integer (int): Whole numbers
    age = 30
    print(f"Integer (int): {age} (type: {type(age)})")

    # b) Float (float): Numbers with a decimal point
    price = 19.99
    print(f"Float (float): {price} (type: {type(price)})")

    # c) String (str): A sequence of characters, enclosed in single or double quotes
    name = "Alice"
    print(f"String (str): '{name}' (type: {type(name)})")

    # d) Boolean (bool): Represents True or False
    is_active = True
    print(f"Boolean (bool): {is_active} (type: {type(is_active)})")
    print("-" * 20)

    # 3. Collection Data Types

    # a) List (list): An ordered, mutable (changeable) collection of items.
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")  # Lists are mutable
    print(f"List (list): {fruits} (type: {type(fruits)})")

    # b) Tuple (tuple): An ordered, immutable (unchangeable) collection of items.
    coordinates = (10.0, 20.0)
    # coordinates.append(30.0)  # This would cause an error!
    print(f"Tuple (tuple): {coordinates} (type: {type(coordinates)})")

    # c) Dictionary (dict): An unordered collection of key-value pairs.
    person = {
        "name": "Bob",
        "age": 25,
        "is_student": False
    }
    person["city"] = "New York" # Dictionaries are mutable
    print(f"Dictionary (dict): {person} (type: {type(person)})")
    print(f"Accessing a value by key: person['name'] = {person['name']}")
    print("-" * 20)

    # 4. Type Casting
    # You can convert values from one type to another.

    # Convert float to int (truncates the decimal)
    num_float = 9.81
    num_int = int(num_float)
    print(f"Original float: {num_float}, cast to int: {num_int}")

    # Convert int to str
    count = 10
    count_str = str(count)
    print(f"Original int: {count}, cast to str: '{count_str}'")

    # Convert str to int (only works if the string contains a valid integer)
    num_str = "123"
    value = int(num_str)
    print(f"Original string: '{num_str}', cast to int: {value}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)