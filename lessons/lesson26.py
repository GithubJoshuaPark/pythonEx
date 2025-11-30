# lessons/lesson26.py
import json
import csv
import os
import utils

utils.show_base_name(__file__, True)

# To work with APIs, we'll use the 'requests' library.
# If you don't have it, install it: pip install requests
try:
    import requests
except ImportError:
    requests = None

def main():
    """
    This lesson demonstrates working with JSON, CSV, and basic web APIs in Python.
    """
    print("--- Lesson 26: Working with JSON, CSV, and APIs ---")

    # --- Part 1: JSON (JavaScript Object Notation) ---
    # JSON is a lightweight data-interchange format, easy for humans to read and write,
    # and easy for machines to parse and generate. It's very similar to Python dictionaries.

    print("\n--- Part 1: JSON ---")

    # Python dictionary to work with
    person_data = {
        "name": "Alice",
        "age": 30,
        "is_student": False,
        "courses": ["History", "Math"],
        "address": {
            "city": "New York",
            "zip": "10001"
        }
    }

    # a) Convert Python dict to JSON string (serialization)
    json_string = json.dumps(person_data, indent=4) # indent makes it readable
    print("\na) Python dict converted to JSON string:")
    print(json_string)

    # b) Parse JSON string back into a Python dict (deserialization)
    parsed_data = json.loads(json_string)
    print(f"\nb) Parsed JSON string back to Python dict. Name: {parsed_data['name']}")

    # c) Write Python dict to a JSON file
    json_filename = "example.json"
    with open(json_filename, 'w') as f:
        json.dump(person_data, f, indent=4)
    print(f"\nc) Data written to '{json_filename}'")

    # d) Read from a JSON file into a Python dict
    with open(json_filename, 'r') as f:
        data_from_file = json.load(f)
    print(f"d) Data read from '{json_filename}'. City: {data_from_file['address']['city']}")
    print("-" * 20)

    # --- Part 2: CSV (Comma-Separated Values) ---
    # CSV is a simple format for storing tabular data. Each line is a data record,
    # and each record consists of one or more fields, separated by commas.

    print("\n--- Part 2: CSV ---")
    csv_filename = "example.csv"

    # Data to write to CSV (list of dictionaries)
    csv_data = [
        {'name': 'Bob', 'age': '25', 'city': 'London'},
        {'name': 'Charlie', 'age': '35', 'city': 'Tokyo'},
        {'name': 'Diana', 'age': '28', 'city': 'Paris'}
    ]
    headers = ['name', 'age', 'city']

    # a) Writing to a CSV file using DictWriter
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader() # Write the header row
        writer.writerows(csv_data) # Write all data rows
    print(f"\na) Data written to '{csv_filename}' using DictWriter.")

    # b) Reading from a CSV file using DictReader
    print(f"\nb) Reading data from '{csv_filename}' using DictReader:")
    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Each row is an OrderedDict or dict
            print(f"  - Name: {row['name']}, Age: {row['age']}, City: {row['city']}")
    print("-" * 20)

    # --- Part 3: Working with APIs ---
    # An API (Application Programming Interface) allows different applications to
    # communicate with each other. Web APIs are commonly accessed via HTTP.

    print("\n--- Part 3: Working with APIs (using 'requests') ---")
    if requests is None:
        print("  'requests' library not found. Please install it to run this part:")
        print("  pip install requests")
    else:
        # We will use JSONPlaceholder, a free fake API for testing
        api_url = "https://jsonplaceholder.typicode.com/posts/1"
        print(f"\na) Making a GET request to: {api_url}")
        try:
            response = requests.get(api_url)
            # Check if the request was successful (status code 200)
            response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)

            print("  Request successful!")
            # The response content is often JSON, which can be parsed into a dict
            post_data = response.json()
            print("\nb) Parsed JSON response from API:")
            print(f"  User ID: {post_data.get('userId')}")
            print(f"  Title: {post_data.get('title')}")
            print(f"  Body: {post_data.get('body', '').strip()[:50]}...") # Show first 50 chars of body

        except requests.exceptions.RequestException as e:
            print(f"  An error occurred while making the API request: {e}")
    print("-" * 20)

    # Clean up created files
    print("\nCleaning up created files...")
    if os.path.exists(json_filename):
        os.remove(json_filename)
        print(f"Removed '{json_filename}'")
    if os.path.exists(csv_filename):
        os.remove(csv_filename)
        print(f"Removed '{csv_filename}'")

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)