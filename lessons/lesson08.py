# lessons/lesson08.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates lists and various list operations in Python.
    """
    print("--- Lesson 08: Lists and List Operations ---")

    # 1. What are Lists?
    # Lists are ordered, mutable (changeable) collections of items.
    # They can contain items of different data types.

    # Creating lists
    empty_list = []
    fruits = ["apple", "banana", "cherry"]
    mixed_list = [1, "hello", 3.14, True]

    print(f"Empty list: {empty_list}")
    print(f"Fruits list: {fruits}")
    print(f"Mixed list: {mixed_list}")
    print("-" * 20)

    # 2. Accessing Elements (Indexing)
    # List elements are accessed by their index, starting from 0.
    # Negative indexing accesses elements from the end (-1 is the last element).

    my_list = ["a", "b", "c", "d", "e"]
    print(f"my_list: {my_list}")
    print(f"First element (index 0): {my_list[0]}")
    print(f"Last element (index -1): {my_list[-1]}")
    print("-" * 20)

    # 3. Slicing Lists
    # Extracting a portion of a list. [start:end:step]

    print(f"Slice from index 1 to 3 (exclusive): {my_list[1:4]}") # ['b', 'c', 'd']
    print(f"Slice from beginning to index 2 (exclusive): {my_list[:2]}") # ['a', 'b']
    print(f"Slice from index 3 to end: {my_list[3:]}") # ['d', 'e']
    print(f"Slice with step [::2]: {my_list[::2]}") # ['a', 'c', 'e']
    print(f"Reverse a list: {my_list[::-1]}") # ['e', 'd', 'c', 'b', 'a']
    print("-" * 20)

    # 4. Modifying Lists (Lists are Mutable)

    # Changing an element
    fruits[1] = "grape"
    print(f"After changing element at index 1: {fruits}")

    # Adding elements
    fruits.append("mango") # Adds to the end
    print(f"After append('mango'): {fruits}")
    fruits.insert(1, "kiwi") # Inserts at a specific index
    print(f"After insert(1, 'kiwi'): {fruits}")
    more_fruits = ["pear", "plum"]
    fruits.extend(more_fruits) # Adds elements from another iterable
    print(f"After extend(['pear', 'plum']): {fruits}")

    # Removing elements
    fruits.remove("apple") # Removes the first occurrence of a value
    print(f"After remove('apple'): {fruits}")
    popped_fruit = fruits.pop(0) # Removes and returns element at index (last by default)
    print(f"After pop(0): {fruits}, Popped: {popped_fruit}")
    del fruits[2] # Deletes element at a specific index
    print(f"After del fruits[2]: {fruits}")
    # del fruits # Deletes the entire list object
    fruits.clear() # Removes all elements, list remains empty
    print(f"After clear(): {fruits}")
    print("-" * 20)

    # Re-initialize for further examples
    numbers = [3, 1, 4, 1, 5, 9, 2]

    # 5. List Operations

    # Concatenation (+)
    list1 = [1, 2]
    list2 = [3, 4]
    combined_list = list1 + list2
    print(f"List concatenation ([1, 2] + [3, 4]): {combined_list}")

    # Repetition (*)
    repeated_list = [0] * 5
    print(f"List repetition ([0] * 5): {repeated_list}")

    # Membership (in, not in)
    print(f"Is 4 in numbers: {4 in numbers}")
    print(f"Is 10 not in numbers: {10 not in numbers}")

    # len(): Returns the number of elements
    print(f"Length of numbers: {len(numbers)}")
    print("-" * 20)

    # 6. Built-in Functions with Lists

    # min(), max(), sum()
    print(f"Min of numbers: {min(numbers)}")
    print(f"Max of numbers: {max(numbers)}")
    print(f"Sum of numbers: {sum(numbers)}")

    # sorted(): Returns a new sorted list (original list unchanged)
    sorted_numbers = sorted(numbers)
    print(f"Original numbers: {numbers}")
    print(f"Sorted numbers (new list): {sorted_numbers}")
    print("-" * 20)

    # 7. List Methods (modifying the list in-place)

    # sort(): Sorts the list in-place
    numbers.sort()
    print(f"After numbers.sort(): {numbers}")
    numbers.sort(reverse=True) # Sort in descending order
    print(f"After numbers.sort(reverse=True): {numbers}")

    # reverse(): Reverses the order of elements in-place
    numbers = [3, 1, 4]
    numbers.reverse()
    print(f"After numbers.reverse(): {numbers}")

    # count(): Returns the number of times a specified value appears
    numbers_with_duplicates = [1, 2, 2, 3, 1, 4, 2]
    print(f"numbers_with_duplicates: {numbers_with_duplicates}")
    print(f"Count of 2: {numbers_with_duplicates.count(2)}")

    # index(): Returns the index of the first occurrence of a value
    print(f"Index of first 1: {numbers_with_duplicates.index(1)}")

    # copy(): Returns a shallow copy of the list
    original_list = [10, 20, 30]
    copied_list = original_list.copy()
    copied_list.append(40)
    print(f"Original list after copy and modification: {original_list}")
    print(f"Copied list: {copied_list}")
    print("-" * 20)

    # 8. Nested Lists
    # Lists can contain other lists.

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Matrix: {matrix}")
    print(f"Accessing element at [0][1]: {matrix[0][1]}") # Output: 2
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)