# lessons/lesson12.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson demonstrates various aspects of function parameters and return values in Python.
    """
    print("--- Lesson 12: Function Parameters and Return Values ---")

    # 1. Positional and Keyword Arguments
    # When calling a function, arguments can be passed by position or by keyword.

    def describe_pet(animal_type, pet_name):
        """Display information about a pet."""
        print(f"I have a {animal_type}.")
        print(f"Its name is {pet_name}.")

    print("\n--- Positional Arguments ---")
    describe_pet("hamster", "Harry") # Arguments passed by position
    print("\n--- Keyword Arguments ---")
    describe_pet(pet_name="Larry", animal_type="dog") # Arguments passed by keyword
    print("-" * 20)

    # 2. Default Parameter Values
    # You can specify a default value for a parameter. This makes the parameter optional.

    def describe_animal(animal_type, pet_name="unknown"):
        """Display information about an animal, with a default pet name."""
        print(f"I have an {animal_type}.")
        print(f"Its name is {pet_name}.")

    print("\n--- Default Parameter Values ---")
    describe_animal("cat", "Whiskers")
    describe_animal("fish") # Uses the default value for pet_name
    print("-" * 20)

    # 3. Arbitrary Positional Arguments (*args)
    # If you don't know how many arguments will be passed into your function,
    # add an * before the parameter name in the function definition.
    # It will receive a tuple of arguments.

    def make_pizza(*toppings):
        """Summarize the pizza we are about to make."""
        print("\n--- Making a pizza with the following toppings: ---")
        for topping in toppings:
            print(f"- {topping}")

    make_pizza("pepperoni")
    make_pizza("mushrooms", "green peppers", "extra cheese")
    print("-" * 20)

    # 4. Arbitrary Keyword Arguments (**kwargs)
    # If you don't know how many keyword arguments will be passed into your function,
    # add two asterisks (**) before the parameter name.
    # It will receive a dictionary of arguments.

    def build_profile(first, last, **user_info):
        """Build a dictionary containing everything we know about a user."""
        user_info['first_name'] = first
        user_info['last_name'] = last
        return user_info

    print("\n--- Building a user profile with **kwargs ---")
    user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
    print(user_profile)
    print("-" * 20)

    # 5. Functions with Return Values
    # A function can return a value or values using the 'return' statement.

    def get_formatted_name(first_name, last_name):
        """Return a full name, neatly formatted."""
        full_name = f"{first_name} {last_name}"
        return full_name.title()

    print("\n--- Function with a single return value ---")
    musician = get_formatted_name("jimi", "hendrix")
    print(musician)
    print("-" * 20)

    # 6. Returning Multiple Values (as a tuple)
    # Python functions can effectively return multiple values by packing them into a tuple.

    def calculate_stats(numbers):
        """Calculate min, max, and sum of a list of numbers."""
        if not numbers:
            return None, None, None # Return multiple None if list is empty
        min_val = min(numbers)
        max_val = max(numbers)
        total_sum = sum(numbers)
        return min_val, max_val, total_sum

    print("\n--- Function returning multiple values (tuple unpacking) ---")
    data = [1, 5, 2, 8, 3]
    minimum, maximum, total = calculate_stats(data)
    print(f"Numbers: {data}")
    print(f"Min: {minimum}, Max: {maximum}, Sum: {total}")

    empty_data = []
    min_empty, max_empty, sum_empty = calculate_stats(empty_data)
    print(f"Empty data stats: Min={min_empty}, Max={max_empty}, Sum={sum_empty}")
    print("-" * 20)

    # 7. 'return' Statement for Early Exit
    # A 'return' statement immediately exits the function.

    def check_age(age):
        """Check if a person is old enough to vote."""
        if age < 18:
            print("You are too young to vote.")
            return # Exit the function early
        print("You are old enough to vote!")

    print("\n--- 'return' for early exit ---")
    check_age(16)
    check_age(20)
    print("-" * 20)

    # 8. Positional-Only and Keyword-Only Arguments (Python 3.8+)
    # You can enforce arguments to be passed positionally or by keyword using / and * respectively.

    def standard_arg(arg):
        print(arg)

    def pos_only_arg(arg, /): # 'arg' must be positional
        print(arg)

    def kw_only_arg(*, arg): # 'arg' must be keyword
        print(arg)

    def combined_args(pos1, pos2, /, standard, *, kw1, kw2):
        """
        pos1, pos2: positional-only
        standard: can be positional or keyword
        kw1, kw2: keyword-only
        """
        print(f"pos1: {pos1}, pos2: {pos2}")
        print(f"standard: {standard}")
        print(f"kw1: {kw1}, kw2: {kw2}")

    print("\n--- Positional-only and Keyword-only arguments ---")
    standard_arg(10)       # Positional
    standard_arg(arg=10)   # Keyword

    pos_only_arg(20)       # Positional is ok
    try:
        pos_only_arg(arg=20) # Keyword will raise TypeError
    except TypeError as e:
        print(f"TypeError for pos_only_arg with keyword: {e}")

    kw_only_arg(arg=30)    # Keyword is ok
    try:
        kw_only_arg(30)      # Positional will raise TypeError
    except TypeError as e:
        print(f"TypeError for kw_only_arg with positional: {e}")

    print("\n--- Combined Arguments ---")
    combined_args(1, 2, 3, kw1=4, kw2=5) # 3 is passed positionally to standard
    combined_args(1, 2, standard=3, kw1=4, kw2=5) # 3 is passed by keyword to standard
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)