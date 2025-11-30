import utils

utils.show_base_name(__file__, True)

# lessons/lesson30.py
# This lesson requires numpy and pandas.
# If you don't have them, install them: pip install numpy pandas
try:
    import numpy as np
    import pandas as pd
except ImportError as e:
    print(f"Import Error: {e}")
    print("Please install numpy and pandas to run this lesson: pip install numpy pandas")
    np = None
    pd = None

def main():
    """
    This lesson provides a basic introduction to NumPy and Pandas for data processing.
    """
    print("--- Lesson 30: NumPy and Pandas Intro for Data Processing ---")

    if not np or not pd:
        print("\n--- End of Lesson (Dependencies not installed) ---")
        return

    # --- Part 1: NumPy (Numerical Python) ---
    # NumPy is the fundamental package for scientific computing in Python.
    # It provides a powerful N-dimensional array object.

    print("\n--- Part 1: NumPy ---")

    # a) Creating NumPy arrays
    print("\na) Creating NumPy arrays")
    py_list = [1, 2, 3, 4, 5]
    np_array = np.array(py_list)
    print(f"Python list: {py_list}")
    print(f"NumPy array: {np_array}")
    print(f"Array shape: {np_array.shape}, Array dtype: {np_array.dtype}")

    # b) Array operations (element-wise)
    print("\nb) Array operations")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"arr1 + arr2 = {arr1 + arr2}")
    print(f"arr1 * 2 = {arr1 * 2}")

    # c) Indexing and Slicing
    print("\nc) Indexing and Slicing")
    print(f"Element at index 1: {np_array[1]}")
    print(f"Slice from index 1 to 3: {np_array[1:4]}")

    # d) Useful NumPy functions
    print("\nd) Useful NumPy functions")
    print(f"np.arange(5): {np.arange(5)}")
    print(f"np.zeros((2, 3)): \n{np.zeros((2, 3))}")
    print(f"np.mean(np_array): {np.mean(np_array)}")
    print("-" * 20)

    # --- Part 2: Pandas ---
    # Pandas is a powerful library for data manipulation and analysis.
    # It introduces two main data structures: Series and DataFrame.

    print("\n--- Part 2: Pandas ---")

    # a) Pandas Series (a 1D labeled array)
    print("\na) Pandas Series")
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print(s)
    print(f"Value at index 'b': {s['b']}")

    # b) Pandas DataFrame (a 2D labeled data structure)
    print("\nb) Pandas DataFrame")
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'age': [25, 30, 35, 28],
        'city': ['New York', 'London', 'Tokyo', 'Paris']
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

    # c) Selecting Data from a DataFrame
    print("\nc) Selecting Data")
    # Select a column
    print("\nSelecting 'name' column:")
    print(df['name'])
    # Select rows using .loc (by label/index)
    print(f"\nSelecting row with index 1 (using .loc):\n{df.loc[1]}")
    # Select rows using .iloc (by position)
    print(f"\nSelecting row at position 2 (using .iloc):\n{df.iloc[2]}")

    # d) Filtering Data
    print("\nd) Filtering Data")
    print("\nPeople older than 28:")
    print(df[df['age'] > 28])

    # e) Basic Statistics
    print("\ne) Basic Statistics")
    print("Descriptive statistics for 'age' column:")
    print(df['age'].describe())

    # f) Adding a new column
    print("\nf) Adding a new column")
    df['is_student'] = [True, False, False, True]
    print(df)
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)