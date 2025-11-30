# lessons/lesson23.py
import unittest
import sys
import utils

utils.show_base_name(__file__, True)

# --- Code to be tested ---
# In a real project, this would likely be in a separate file (e.g., 'utils.py').
def add(a, b):
    """Returns the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

def is_palindrome(s):
    """Returns True if the string is a palindrome, False otherwise."""
    return s == s[::-1]

# --- Part 1: unittest ---
# 'unittest' is a test framework built into the Python standard library.

class TestMyFunctions(unittest.TestCase):
    """Test case for our simple functions."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-10, 10), 0)

    def test_add_type_error(self):
        """Test that add() raises a TypeError for non-numeric input."""
        with self.assertRaises(TypeError):
            add("a", "b")
        with self.assertRaises(TypeError):
            add(1, "b")

    def test_is_palindrome_true(self):
        """Test cases where is_palindrome should return True."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_false(self):
        """Test cases where is_palindrome should return False."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))


def main():
    """
    This lesson demonstrates unit testing with Python's built-in 'unittest'
    and provides an introduction to 'pytest'.
    """
    print("--- Lesson 23: Unit Tests with unittest and pytest ---")
    print("\n--- Part 1: unittest ---")
    print("This file contains test cases written using the 'unittest' framework.")
    print("To run these tests from your command line, use the command:")
    print("  python -m unittest lessons/lesson23.py")
    print("\nRunning tests now...\n")

    # This creates a TestSuite and runs it.
    # Note: Running tests directly from the script can be complex.
    # The standard way is using 'python -m unittest'.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyFunctions)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if not result.wasSuccessful():
        print("\nSome tests failed. Please review the output above.")
    else:
        print("\nAll unittest tests passed successfully!")

    print("-" * 20)

    print("\n--- Part 2: pytest ---")
    print("pytest is a popular third-party testing framework.")
    print("To use it, you first need to install it: pip install pytest")
    print("\nKey advantages of pytest:")
    print("- Less boilerplate: No need for classes or 'self'.")
    print("- Simple 'assert' statements instead of 'self.assertEqual', etc.")
    print("- Powerful features like fixtures and plugins.")
    print("\nBelow is how you would write the same tests in pytest style:")
    print("(This is for demonstration; it won't be run by this script.)")

    pytest_style_code = """
# --- Pytest Style Example (for demonstration) ---
# To run this, you would save it in a file like 'test_app.py'
# and run 'pytest' from your terminal.

import pytest
# from your_module import add, is_palindrome  # Assumes functions are in another file

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", "b")

def test_is_palindrome_true():
    assert is_palindrome("racecar")

def test_is_palindrome_false():
    assert not is_palindrome("hello")
"""
    print(pytest_style_code)
    print("To run pytest, you would save the above code in a file (e.g., test_lesson23.py) and run 'pytest' in your terminal.")
    print("Pytest automatically discovers and runs test files and functions.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    # If run as the main script, execute the lesson's main function.
    # unittest can discover and run tests without this block.
    # We include it to make the lesson runnable via `python lessons/lesson23.py`
    # and to show the test results within the lesson flow.
    main()
else:
    utils.show_base_name(__file__, False)