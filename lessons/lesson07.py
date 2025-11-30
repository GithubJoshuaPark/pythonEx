# lessons/lesson07.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates while loops and for loops in Python.
    """
    print("--- Lesson 07: While Loops and For Loops ---")

    # 1. While Loop
    # A while loop repeatedly executes a block of code as long as a condition is true.

    print("--- While Loop Example ---")
    count = 0
    while count < 5:
        print(f"Count is: {count}")
        count += 1 # Important: Don't forget to update the condition variable!
    print("While loop finished.")
    print("-" * 20)

    # While loop with 'break'
    # The 'break' statement is used to exit the loop prematurely.
    print("--- While Loop with 'break' ---")
    i = 0
    while True: # Infinite loop until break is encountered
        print(f"i is: {i}")
        if i == 3:
            print("Breaking the loop when i is 3.")
            break
        i += 1
    print("Loop broken.")
    print("-" * 20)

    # While loop with 'continue'
    # The 'continue' statement skips the rest of the current iteration
    # and proceeds to the next iteration.
    print("--- While Loop with 'continue' ---")
    j = 0
    while j < 5:
        j += 1
        if j == 3:
            print(f"Skipping j = {j}")
            continue
        print(f"j is: {j}")
    print("Loop with continue finished.")
    print("-" * 20)

    # 2. For Loop
    # A for loop is used for iterating over a sequence (that is, a list, tuple, dictionary, set, or string).

    print("--- For Loop Example (iterating over a list) ---")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I like {fruit}.")
    print("For loop over list finished.")
    print("-" * 20)

    print("--- For Loop Example (iterating over a string) ---")
    word = "Python"
    for char in word:
        print(f"Character: {char}")
    print("For loop over string finished.")
    print("-" * 20)

    # For loop with range()
    # range(stop): 0 to stop-1
    # range(start, stop): start to stop-1
    # range(start, stop, step): start to stop-1, with step
    print("--- For Loop with range() ---")
    for k in range(5): # 0, 1, 2, 3, 4
        print(f"Number from range(5): {k}")

    print("--- For Loop with range(start, stop) ---")
    for l in range(2, 7): # 2, 3, 4, 5, 6
        print(f"Number from range(2, 7): {l}")

    print("--- For Loop with range(start, stop, step) ---")
    for m in range(0, 10, 2): # 0, 2, 4, 6, 8
        print(f"Number from range(0, 10, 2): {m}")
    print("For loop with range finished.")
    print("-" * 20)

    # For loop with 'break' and 'continue'
    print("--- For Loop with 'break' and 'continue' ---")
    numbers = [1, 2, 3, -4, 5, 0, 6]
    for num in numbers:
        if num < 0:
            print(f"Negative number {num} found, breaking loop.")
            break
        if num == 0:
            print(f"Zero found, skipping to next number.")
            continue
        print(f"Processing number: {num}")
    print("For loop with break/continue finished.")
    print("-" * 20)

    # 3. Nested Loops
    # A loop inside another loop.

    print("--- Nested Loops Example ---")
    for row in range(3):
        for col in range(2):
            print(f"({row}, {col})", end=" ")
        print() # Newline after each row
    print("Nested loops finished.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)