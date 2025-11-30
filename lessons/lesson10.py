# lessons/lesson10.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates dictionaries and various dictionary methods in Python.
    """
    print("--- Lesson 10: Dictionaries and Dictionary Methods ---")

    # 1. What are Dictionaries?
    # Dictionaries are collections of key-value pairs.
    # They are mutable (changeable).
    # Keys must be unique and immutable (e.g., strings, numbers, tuples).
    # Since Python 3.7, dictionaries are ordered. In 3.6 and earlier, they were unordered.

    # Creating dictionaries
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    empty_dict = {}

    print(f"person dictionary: {person}")
    print(f"Empty dictionary: {empty_dict}")
    print("-" * 20)

    # 2. Accessing Values
    # Values are accessed using their corresponding keys.

    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")

    # Using the get() method (safer, avoids KeyError)
    print(f"City (using get()): {person.get('city')}")
    # If the key does not exist, get() returns None by default, or a specified default value.
    print(f"Country (using get()): {person.get('country')}") # Returns None
    print(f"Country (get() with default): {person.get('country', 'USA')}")
    print("-" * 20)

    # 3. Modifying Dictionaries
    # Dictionaries are mutable.

    # Changing a value
    person['age'] = 26
    print(f"After changing age: {person}")

    # Adding a new key-value pair
    person['email'] = 'alice@example.com'
    print(f"After adding email: {person}")

    # Removing items
    popped_value = person.pop('city') # Removes 'city' and returns its value
    print(f"After pop('city'): {person}, Popped value: {popped_value}")
    # popitem() removes and returns the last inserted key-value pair (in Python 3.7+)
    popped_item = person.popitem()
    print(f"After popitem(): {person}, Popped item: {popped_item}")
    # 'del' statement
    del person['age']
    print(f"After del person['age']: {person}")
    # 'clear()' removes all items
    person.clear()
    print(f"After clear(): {person}")
    print("-" * 20)

    # Re-initialize for further examples
    person = {
        "name": "Bob",
        "age": 30,
        "city": "London"
    }

    # 4. Dictionary Methods

    # keys(): Returns a view object displaying a list of all the keys
    all_keys = person.keys()
    print(f"Keys: {all_keys}")

    # values(): Returns a view object displaying a list of all the values
    all_values = person.values()
    print(f"Values: {all_values}")

    # items(): Returns a view object displaying a list of key-value tuple pairs
    all_items = person.items()
    print(f"Items: {all_items}")
    print("-" * 20)

    # 5. Iterating through Dictionaries

    # Iterating over keys (default)
    print("Iterating over keys:")
    for key in person:
        print(f"  Key: {key}, Value: {person[key]}")

    # Iterating over values
    print("\nIterating over values:")
    for value in person.values():
        print(f"  Value: {value}")

    # Iterating over key-value pairs
    print("\nIterating over items:")
    for key, value in person.items():
        print(f"  Key: {key}, Value: {value}")
    print("-" * 20)

    # 6. Nested Dictionaries
    # Dictionaries can contain other dictionaries.

    employees = {
        'e101': {'name': 'Charlie', 'role': 'Developer'},
        'e102': {'name': 'Diana', 'role': 'Designer'}
    }
    print(f"Nested dictionary: {employees}")
    print(f"Employee e101's name: {employees['e101']['name']}")
    print("-" * 20)

    # 7. update(): Merges a dictionary with another dictionary or an iterable of key-value pairs
    person.update({'age': 31, 'country': 'UK'})
    print(f"After update(): {person}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)