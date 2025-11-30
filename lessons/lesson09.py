# lessons/lesson09.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates tuples, sets, and frozensets in Python.
    """
    print("--- Lesson 09: Tuples, Sets, and Frozensets ---")

    # 1. Tuples
    # Tuples are ordered, immutable (unchangeable) collections of items.
    # They are defined using parentheses ().

    # Creating tuples
    my_tuple = (1, 2, 3, "hello")
    single_element_tuple = (5,) # Comma is essential for single-element tuple
    another_tuple = 10, 20, 30 # Parentheses are optional for tuple packing
    empty_tuple = ()

    print(f"my_tuple: {my_tuple}")
    print(f"Single element tuple: {single_element_tuple}")
    print(f"Another tuple (packed): {another_tuple}")
    print(f"Type of another_tuple: {type(another_tuple)}")
    print("-" * 20)

    # Accessing elements (indexing) and slicing
    print(f"First element of my_tuple: {my_tuple[0]}")
    print(f"Slice of my_tuple (1:3): {my_tuple[1:3]}") # (2, 3)

    # Tuples are immutable, so you cannot change their elements
    try:
        my_tuple[0] = 5
    except TypeError as e:
        print(f"Cannot change tuple elements: {e}")

    # Tuple packing and unpacking
    coordinates = (10, 20)
    x, y = coordinates # Unpacking
    print(f"Unpacked coordinates: x={x}, y={y}")

    # Swapping variables easily with tuples
    a, b = 1, 2
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    print("-" * 20)

    # 2. Sets
    # Sets are unordered collections of unique items. They are mutable.
    # Defined using curly braces {} or the set() constructor.

    # Creating sets
    my_set = {1, 2, 3, 2, 1} # Duplicate elements are automatically removed
    print(f"my_set: {my_set}") # Output might be {1, 2, 3} (order not guaranteed)

    # Creating from a list
    numbers_list = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = set(numbers_list)
    print(f"Unique numbers from list: {unique_numbers}")
    print("-" * 20)

    # Adding and removing elements
    my_set.add(4)
    print(f"After adding 4: {my_set}")
    my_set.remove(2) # Raises KeyError if element not found
    print(f"After removing 2: {my_set}")
    my_set.discard(10) # Does nothing if element not found (no error)
    print(f"After discarding 10: {my_set}")
    popped_item = my_set.pop() # Removes and returns an arbitrary element
    print(f"Popped item from set: {popped_item}, set now: {my_set}")
    print("-" * 20)

    # Set operations
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    print(f"Set A: {set_a}, Set B: {set_b}")
    print(f"Union (A | B): {set_a.union(set_b)}") # Elements in A or B or both
    print(f"Intersection (A & B): {set_a.intersection(set_b)}") # Elements common to A and B
    print(f"Difference (A - B): {set_a.difference(set_b)}") # Elements in A but not in B
    print(f"Symmetric Difference (A ^ B): {set_a.symmetric_difference(set_b)}") # Elements in A or B but not both
    print("-" * 20)

    # Subset and Superset
    set_c = {1, 2}
    print(f"Set C: {set_c}")
    print(f"C is subset of A (C <= A): {set_c.issubset(set_a)}")
    print(f"A is superset of C (A >= C): {set_a.issuperset(set_c)}")
    print("-" * 20)

    # 3. Frozensets
    # Frozensets are immutable versions of sets. Once created, their elements cannot be changed.
    # They can be used as dictionary keys or elements of another set.

    # Creating frozensets
    frozen_set = frozenset([1, 2, 3, 2])
    print(f"frozen_set: {frozen_set}")

    # Cannot add or remove elements
    try:
        frozen_set.add(4)
    except AttributeError as e:
        print(f"Cannot add to frozenset: {e}")

    # Frozensets can be elements of a set
    set_of_frozensets = {frozenset({1, 2}), frozenset({3, 4})}
    print(f"Set of frozensets: {set_of_frozensets}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)