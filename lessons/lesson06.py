# lessons/lesson06.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates if statements and comparison operators in Python.
    """
    print("--- Lesson 06: If Statements and Comparisons ---")

    # 1. Comparison Operators
    # These operators compare two values and return a Boolean (True or False).
    x = 10
    y = 12
    z = 10

    print(f"Given x = {x}, y = {y}, z = {z}")

    print(f"x == y (equal to): {x == y}")       # False
    print(f"x != y (not equal to): {x != y}")    # True
    print(f"x < y (less than): {x < y}")         # True
    print(f"x > y (greater than): {x > y}")       # False
    print(f"x <= z (less than or equal to): {x <= z}") # True
    print(f"x >= y (greater than or equal to): {x >= y}") # False
    print("-" * 20)

    # 2. Basic If Statement
    # Executes a block of code if a condition is True.

    score = 75
    if score >= 60:
        print("You passed the exam!")
    print("-" * 20)

    # 3. If-Else Statement
    # Executes one block of code if the condition is True,
    # and another block if it's False.

    temperature = 28
    if temperature > 30:
        print("It's a hot day!")
    else:
        print("It's not too hot today.")
    print("-" * 20)

    # 4. If-Elif-Else Statement
    # Handles multiple conditions. 'elif' stands for 'else if'.

    grade = 85
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
    print("-" * 20)

    # 5. Logical Operators: and, or, not
    # Combine conditional statements.

    age = 20
    has_license = True

    # 'and': Both conditions must be True
    if age >= 18 and has_license:
        print("You are an adult and can drive.")

    # 'or': At least one condition must be True
    if age < 18 or not has_license:
        print("You are either not an adult or cannot drive.")

    # 'not': Reverses the boolean result
    is_sunny = False
    if not is_sunny:
        print("It's not sunny today.")
    print("-" * 20)

    # 6. Nested If Statements
    # An if statement inside another if statement.

    balance = 1000
    withdrawal_amount = 300
    pin_correct = True

    if pin_correct:
        if withdrawal_amount <= balance:
            print(f"Withdrawing ${withdrawal_amount}.")
            balance -= withdrawal_amount
            print(f"New balance: ${balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Incorrect PIN.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)