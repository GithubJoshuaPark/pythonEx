# lessons/lesson05.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates strings and various string methods in Python.
    """
    print("--- Lesson 05: Strings and String Methods ---")

    # 1. What are Strings?
    # Strings are sequences of characters, used for storing text information.
    # They are immutable, meaning once created, their content cannot be changed.

    # 2. Creating Strings
    # Single quotes
    str1 = 'Hello, World!'
    # Double quotes
    str2 = "Python Programming"
    # Triple quotes (for multi-line strings or docstrings)
    str3 = """This is a multi-line
string example."""

    print(f"str1: {str1}")
    print(f"str2: {str2}")
    print(f"str3: {str3}")
    print("-" * 20)

    # 3. String Concatenation
    # Joining strings together
    full_string = str1 + " " + str2
    print(f"Concatenated string: {full_string}")

    # Using f-strings (formatted string literals) for easy combination
    name = "Alice"
    age = 30
    greeting = f"My name is {name} and I am {age} years old."
    print(f"f-string example: {greeting}")
    print("-" * 20)

    # 4. String Indexing and Slicing
    my_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Indexing: Accessing individual characters
    print(f"my_string: {my_string}")
    print(f"First character (index 0): {my_string[0]}")
    print(f"Last character (index -1): {my_string[-1]}")

    # Slicing: Accessing a substring
    # [start:end] (end is exclusive)
    print(f"Slice from index 2 to 5 (exclusive): {my_string[2:6]}") # CDEF
    print(f"Slice from beginning to index 5 (exclusive): {my_string[:5]}") # ABCDE
    print(f"Slice from index 20 to end: {my_string[20:]}") # UVWXYZ
    print(f"Slice with step [start:end:step]: {my_string[::2]}") # ACEGI...
    print(f"Reverse a string: {my_string[::-1]}") # ZYXWV...
    print("-" * 20)

    # 5. Common String Methods

    sample_text = "  Python is FUN!  "

    # len(): Returns the length of the string (built-in function)
    print(f"Original: '{sample_text}', Length: {len(sample_text)}")

    # strip(): Removes leading/trailing whitespace
    stripped_text = sample_text.strip()
    print(f"strip(): '{stripped_text}', Length: {len(stripped_text)}")

    # lower(), upper(), capitalize(), title()
    print(f"lower(): '{stripped_text.lower()}'")
    print(f"upper(): '{stripped_text.upper()}'")
    print(f"capitalize(): '{stripped_text.capitalize()}'") # Capitalizes only the first letter of the string
    print(f"title(): '{stripped_text.title()}'")           # Capitalizes the first letter of each word
    print("-" * 20)

    # find(): Returns the lowest index of a substring if found, -1 otherwise
    print(f"find('is'): {stripped_text.find('is')}")
    print(f"find('xyz'): {stripped_text.find('xyz')}")

    # replace(): Replaces all occurrences of a substring
    replaced_text = stripped_text.replace("FUN", "AWESOME")
    print(f"replace('FUN', 'AWESOME'): '{replaced_text}'")

    # split(): Splits the string into a list of substrings
    words = "apple,banana,cherry".split(',')
    print(f"split(','): {words}")
    sentence_words = stripped_text.split() # Splits by whitespace by default
    print(f"split(): {sentence_words}")

    # join(): Joins elements of an iterable (e.g., a list) with the string as a separator
    joined_string = "-".join(["one", "two", "three"])
    print(f"'-'.join(['one', 'two', 'three']): {joined_string}")
    print("-" * 20)

    # startswith(), endswith()
    print(f"'Python'.startswith('Py'): {'Python'.startswith('Py')}")
    print(f"'Python'.endswith('on'): {'Python'.endswith('on')}")

    # isalpha(), isdigit(), isalnum() (checks if all characters are alphabetic, digits, or alphanumeric)
    print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")
    print(f"'123'.isdigit(): {'123'.isdigit()}")
    print(f"'Python3'.isalnum(): {'Python3'.isalnum()}")
    print(f"'Python 3'.isalnum(): {'Python 3'.isalnum()} (space is not alphanumeric)")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)