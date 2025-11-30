# lessons/lesson13.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates lambda functions and various built-in functions in Python.
    """
    print("--- Lesson 13: Lambda Functions and Built-in Functions ---")

    # 1. Lambda Functions (Anonymous Functions)
    # A lambda function is a small anonymous function.
    # It can take any number of arguments, but can only have one expression.
    # Syntax: lambda arguments : expression

    # Basic lambda function
    add_two_numbers = lambda a, b: a + b
    print(f"Lambda add_two_numbers(5, 3): {add_two_numbers(5, 3)}")

    # Using lambda with sorted()
    points = [(1, 2), (3, 1), (5, 0), (0, 4)]
    # Sort by the second element (y-coordinate)
    sorted_points = sorted(points, key=lambda point: point[1])
    print(f"Sorted points by y-coordinate: {sorted_points}")

    # Using lambda with filter()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers from list: {even_numbers}")

    # Using lambda with map()
    squared_numbers = list(map(lambda x: x * x, numbers))
    print(f"Squared numbers from list: {squared_numbers}")
    print("-" * 20)

    # 2. Built-in Functions
    # Python comes with many built-in functions that are always available.
    # We've already seen some (print, input, len, type, int, float, str, bool, min, max, sum, abs, round).

    # range(): Generates a sequence of numbers (used primarily in for loops).
    print("\n--- range() ---")
    for i in range(3): # 0, 1, 2
        print(f"range(3) output: {i}")

    # zip(): Combines multiple iterables into a single iterator of tuples.
    print("\n--- zip() ---")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")

    # enumerate(): Adds a counter to an iterable and returns it as an enumerate object.
    print("\n--- enumerate() ---")
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    print("-" * 20)

    # all(): Returns True if all elements of an iterable are true (or if the iterable is empty).
    print("\n--- all() ---")
    list1 = [True, True, True]
    list2 = [True, False, True]
    print(f"all([True, True, True]): {all(list1)}")
    print(f"all([True, False, True]): {all(list2)}")

    # any(): Returns True if any element of an iterable is true. If the iterable is empty, returns False.
    print("\n--- any() ---")
    print(f"any([True, False, True]): {any(list2)}")
    print(f"any([False, False]): {any([False, False])}")
    print("-" * 20)

    # isinstance(): Checks if an object is an instance of a class or a type.
    print("\n--- isinstance() ---")
    my_var = "hello"
    print(f"isinstance('{my_var}', str): {isinstance(my_var, str)}")
    print(f"isinstance({my_var}, int): {isinstance(my_var, int)}")

    # id(): Returns the identity of an object (its memory address).
    print("\n--- id() ---")
    a = 10
    b = a
    c = 10
    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}") # Same as a, because b refers to the same object
    print(f"id(c): {id(c)}") # Often same as a and b due to integer caching
    print("-" * 20)

    # pow(): Returns the value of x to the power of y (x**y).
    print("\n--- pow() ---")
    print(f"pow(2, 3): {pow(2, 3)}") # 2^3 = 8
    print(f"pow(4, 0.5): {pow(4, 0.5)}") # Square root of 4 = 2.0
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)