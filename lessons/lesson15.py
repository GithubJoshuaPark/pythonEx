# lessons/lesson15.py
import os
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates how to read from and write to files in Python.
    """
    print("--- Lesson 15: Working with Files (Read/Write) ---")

    file_name = "example.txt"
    write_data = "Hello, file world!\n" \
                 "This is a second line.\n" \
                 "And a third line for good measure."

    # 1. Writing to a file (Mode 'w')
    # 'w' mode opens the file for writing. If the file exists, its content is truncated (emptied).
    # If the file does not exist, a new one is created.
    # It's crucial to close the file after writing or use 'with' statement.

    print("\n--- Writing to a file (Mode 'w') ---")
    try:
        with open(file_name, 'w') as file:
            file.write(write_data)
        print(f"Successfully wrote to '{file_name}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")
    print("-" * 20)

    # 2. Reading from a file (Mode 'r')
    # 'r' mode opens the file for reading (default mode).

    print("\n--- Reading from a file (Mode 'r') ---")
    try:
        with open(file_name, 'r') as file:
            content = file.read() # Reads the entire content of the file
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found for reading.")
    except IOError as e:
        print(f"Error reading from file: {e}")
    print("-" * 20)

    # 3. Appending to a file (Mode 'a')
    # 'a' mode opens the file for appending. If the file exists, new content is
    # written at the end. If the file does not exist, a new one is created.

    print("\n--- Appending to a file (Mode 'a') ---")
    append_data = "\nThis is an appended line."
    try:
        with open(file_name, 'a') as file:
            file.write(append_data)
        print(f"Successfully appended to '{file_name}'.")
        with open(file_name, 'r') as file:
            print(f"Content after appending:\n{file.read()}")
    except IOError as e:
        print(f"Error appending to file: {e}")
    print("-" * 20)

    # 4. Reading Line by Line
    # Useful for large files, avoids loading entire file into memory.

    print("\n--- Reading line by line ---")
    lines_read = []
    try:
        with open(file_name, 'r') as file:
            for line in file: # Iterate over file object
                lines_read.append(line.strip()) # .strip() removes newline characters
        print("Lines read:")
        for l in lines_read:
            print(f"  '{l}'")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found for reading.")
    print("-" * 20)

    # 5. Using readlines()
    # Reads all lines and returns them as a list of strings, each including the newline char.

    print("\n--- Using readlines() ---")
    try:
        with open(file_name, 'r') as file:
            all_lines = file.readlines()
        print("Lines from readlines():")
        for l in all_lines:
            print(f"  '{l.strip()}'") # Strip to remove newlines for cleaner output
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    print("-" * 20)

    # 6. Handling File Not Found Error
    # It's good practice to handle potential errors like a file not existing.

    non_existent_file = "non_existent.txt"
    print(f"\n--- Trying to open '{non_existent_file}' ---")
    try:
        with open(non_existent_file, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Caught expected error: '{non_existent_file}' does not exist.")
    print("-" * 20)

    # 7. Other file operations from 'os' module
    # Check if a file exists
    print(f"Does '{file_name}' exist? {os.path.exists(file_name)}")
    print(f"Does '{non_existent_file}' exist? {os.path.exists(non_existent_file)}")

    # Rename a file
    new_file_name = "renamed_example.txt"
    if os.path.exists(file_name):
        os.rename(file_name, new_file_name)
        print(f"Renamed '{file_name}' to '{new_file_name}'.")
    print(f"Does '{new_file_name}' exist? {os.path.exists(new_file_name)}")
    print("-" * 20)

    # Clean up: Remove the created file
    print("\n--- Cleaning up created file ---")
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
        print(f"Removed '{new_file_name}'.")
    print(f"Does '{new_file_name}' exist? {os.path.exists(new_file_name)}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)