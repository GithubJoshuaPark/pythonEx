# lessons/lesson20.py
import sys
import time
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson covers list comprehensions, generators, and iterators in Python.
    """
    print("--- Lesson 20: List Comprehensions, Generators, and Iterators ---")

    # 1. List Comprehensions
    # A concise and elegant way to create lists.
    # Syntax: [expression for item in iterable if condition]

    print("\n--- List Comprehensions ---")
    # Basic example: Squaring numbers
    # Using a for loop
    squares_loop = []
    for x in range(10):
        squares_loop.append(x**2)
    # Using list comprehension
    squares_comp = [x**2 for x in range(10)]
    print(f"Squares (loop): {squares_loop}")
    print(f"Squares (comp): {squares_comp}")

    # Example with a condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # Example with if-else
    numbers_labeled = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
    print(f"Numbers labeled: {numbers_labeled}")

    # Set and Dictionary Comprehensions
    unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3]}
    print(f"Set comprehension: {unique_squares}")
    square_dict = {x: x**2 for x in range(5)}
    print(f"Dictionary comprehension: {square_dict}")
    print("-" * 20)

    # 2. Iterators
    # An iterator is an object that contains a countable number of values.
    # It follows the iterator protocol (__iter__ and __next__ methods).
    # 'for' loops automatically use iterators behind the scenes.

    print("\n--- Iterators ---")
    my_list = [1, 2, 3]
    my_iterator = iter(my_list) # Get an iterator from the list

    print("Manually iterating through my_list:")
    try:
        print(next(my_iterator))
        print(next(my_iterator))
        print(next(my_iterator))
        print(next(my_iterator)) # This will raise StopIteration
    except StopIteration:
        print("StopIteration reached (end of iterator).")
    print("-" * 20)

    # 3. Generators
    # Generators are a special type of iterator, created using a function with 'yield'
    # or with a generator expression. They are lazy and memory-efficient.

    # a) Generator Expressions
    # Syntax is similar to list comprehensions but with parentheses ().
    print("\n--- Generator Expressions ---")
    large_range = 10_000_000

    # List comprehension (builds the entire list in memory)
    start_time = time.time()
    list_comp = [i for i in range(large_range)]
    list_comp_mem = sys.getsizeof(list_comp)
    print(f"List comp memory: {list_comp_mem / 1024 / 1024:.2f} MB, time: {time.time() - start_time:.4f}s")

    # Generator expression (does not build the list, is an object)
    start_time = time.time()
    gen_expr = (i for i in range(large_range))
    gen_expr_mem = sys.getsizeof(gen_expr)
    print(f"Gen expr memory:  {gen_expr_mem} bytes, time: {time.time() - start_time:.4f}s")

    # We can iterate over the generator just like any other iterator.
    # Let's sum the numbers to show it works.
    sum_from_gen = sum(gen_expr)
    print(f"Sum of numbers from generator: {sum_from_gen}")
    print("-" * 20)

    # b) Generator Functions
    # Uses the 'yield' keyword to produce a series of values.
    # The function's state is saved between calls.
    print("\n--- Generator Functions ---")
    def countdown(n):
        """A generator function that counts down from n."""
        print("Starting countdown...")
        while n > 0:
            yield n
            n -= 1
        print("Countdown finished.")

    # Create a generator object
    my_countdown = countdown(3)
    print(f"Generator object created: {my_countdown}")

    # Iterate through the generator
    try:
        print(f"Next value: {next(my_countdown)}")
        print(f"Next value: {next(my_countdown)}")
        print(f"Next value: {next(my_countdown)}")
        print(f"Next value: {next(my_countdown)}") # This will raise StopIteration
    except StopIteration:
        print("Caught StopIteration from countdown generator.")

    # Using the generator in a for loop (more common)
    print("\nUsing countdown in a for loop:")
    for num in countdown(5):
        print(f"  T-minus {num}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)