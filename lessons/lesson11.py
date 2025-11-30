# lessons/lesson11.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates how to define and call functions in Python.
    """
    print("--- Lesson 11: Defining and Calling Functions ---")

    # 1. What is a Function?
    # A function is a block of organized, reusable code that is used to
    # perform a single, related action. Functions provide better modularity
    # for your application and a high degree of code reusing.

    # 2. Defining a Simple Function
    # Functions are defined using the 'def' keyword.

    def greet_user():
        """This function simply prints a greeting message."""
        print("Hello there!")
        print("Welcome to the world of functions.")

    # 3. Calling a Function
    # To execute the code inside a function, you 'call' it.

    print("\nCalling greet_user() for the first time:")
    greet_user()

    print("\nCalling greet_user() again:")
    greet_user()
    print("-" * 20)

    # 4. Function with Parameters
    # Parameters are variables listed inside the parentheses in the function definition.
    # They act as placeholders for the values (arguments) you will pass to the function.

    def greet_name(name):
        """This function greets the person passed in as an argument."""
        print(f"Hello, {name}!")
        print("Nice to meet you.")

    print("\nCalling greet_name() with an argument:")
    greet_name("Alice")
    greet_name("Bob") # Can be called multiple times with different arguments
    print("-" * 20)

    # 5. Function with Multiple Parameters

    def add_numbers(num1, num2):
        """This function takes two numbers and prints their sum."""
        sum_result = num1 + num2
        print(f"The sum of {num1} and {num2} is {sum_result}.")

    print("\nCalling add_numbers() with two arguments:")
    add_numbers(10, 20)
    add_numbers(5.5, 3.2)
    print("-" * 20)

    # 6. Function with a Return Value
    # The 'return' statement is used to send a value back to the caller.

    def multiply_numbers(a, b):
        """This function takes two numbers and returns their product."""
        product = a * b
        return product # The result is sent back

    print("\nCalling multiply_numbers() and storing the result:")
    result1 = multiply_numbers(4, 5)
    print(f"Product of 4 and 5 is: {result1}")

    result2 = multiply_numbers(10, 3)
    print(f"Product of 10 and 3 is: {result2}")
    print(f"Adding the results: {result1 + result2}")
    print("-" * 20)

    # 7. Functions Returning None (Implicit Return)
    # If a function doesn't have an explicit 'return' statement, it implicitly
    # returns None.

    def do_nothing():
        """This function does nothing and implicitly returns None."""
        pass # 'pass' is a null operation; nothing happens when it executes

    print("\nCalling do_nothing() and checking its return value:")
    return_value = do_nothing()
    print(f"Return value of do_nothing(): {return_value}")
    print("-" * 20)

    # 8. Docstrings
    # A string literal as the first statement in a module, function, class,
    # or method definition. Used for documentation.

    def example_function(param):
        """
        This is an example function docstring.
        It explains what the function does and its parameters.

        Args:
            param (str): A string parameter for demonstration.

        Returns:
            str: A modified string.
        """
        return param.upper()

    print("\nAccessing a function's docstring:")
    print(example_function.__doc__)
    print(f"Result of example_function('hello'): {example_function('hello')}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)