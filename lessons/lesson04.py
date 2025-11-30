# lessons/lesson04.py
import math
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates numbers (integers and floats) and basic math operations in Python.
    """
    print("--- Lesson 04: Numbers and Math Operations ---")

    # 1. Numbers: Integers and Floats

    # Integers (int): Whole numbers
    num_int = 10
    print(f"Integer: {num_int} (type: {type(num_int)})")

    # Floats (float): Numbers with a decimal point
    num_float = 20.5
    print(f"Float: {num_float} (type: {type(num_float)})")

    # Python automatically handles large numbers
    large_int = 12345678901234567890
    print(f"Large Integer: {large_int}")
    print("-" * 20)

    # 2. Basic Arithmetic Operations

    a = 15
    b = 4

    print(f"Given a = {a}, b = {b}")

    # Addition
    print(f"Addition (a + b): {a + b}")

    # Subtraction
    print(f"Subtraction (a - b): {a - b}")

    # Multiplication
    print(f"Multiplication (a * b): {a * b}")

    # Division (always returns a float)
    print(f"Division (a / b): {a / b}")

    # Floor Division (returns the integer part of the division)
    print(f"Floor Division (a // b): {a // b}")

    # Modulo (returns the remainder of the division)
    print(f"Modulo (a % b): {a % b}")

    # Exponentiation (a to the power of b)
    print(f"Exponentiation (a ** b): {a ** b}")
    print("-" * 20)

    # 3. Order of Operations (PEMDAS/BODMAS)
    # Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
    result = 10 + 5 * 2 - (6 / 3) ** 2
    # 10 + 10 - (2.0) ** 2
    # 10 + 10 - 4.0
    # 20 - 4.0
    # 16.0
    print(f"Order of Operations (10 + 5 * 2 - (6 / 3) ** 2): {result}")
    print("-" * 20)

    # 4. Built-in Math Functions

    # abs(): Absolute value
    print(f"Absolute value of -7: {abs(-7)}")

    # round(): Round to the nearest integer or a specified number of decimal places
    print(f"Round 3.14159: {round(3.14159)}")
    print(f"Round 3.14159 to 2 decimal places: {round(3.14159, 2)}")

    # min() and max(): Find the minimum or maximum in a sequence
    print(f"Minimum of (10, 5, 20): {min(10, 5, 20)}")
    print(f"Maximum of (10, 5, 20): {max(10, 5, 20)}")
    print("-" * 20)

    # 5. The 'math' Module
    # For more advanced mathematical operations, import the 'math' module.

    # Square root
    print(f"Square root of 25 (math.sqrt): {math.sqrt(25)}")

    # Pi constant
    print(f"Value of Pi (math.pi): {math.pi}")

    # Ceil (smallest integer >= x) and Floor (largest integer <= x)
    print(f"Ceiling of 3.14: {math.ceil(3.14)}")
    print(f"Floor of 3.8: {math.floor(3.8)}")

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)