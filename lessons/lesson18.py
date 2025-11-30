# lessons/lesson18.py
import utils

utils.show_base_name(__file__, True)

def main():
    """
    This lesson introduces the basic concepts of Classes and Objects in Python.
    """
    print("--- Lesson 18: Classes and Objects Basics ---")

    # 1. Introduction to Object-Oriented Programming (OOP)
    # OOP is a programming paradigm based on the concept of "objects",
    # which can contain data (attributes) and code (methods).
    # Key concepts: Classes, Objects, Inheritance, Polymorphism, Encapsulation.

    # 2. Defining a Class
    # A class is a blueprint for creating objects. It defines the structure
    # and behavior that objects of that class will have.
    # Use the 'class' keyword, followed by the class name (conventionally PascalCase).

    class Dog:
        """A simple attempt to model a dog."""
        # Class attribute: shared by all instances of the class
        species = "Canis familiaris"

        def __init__(self, name, age):
            """
            Constructor method. Initializes a new Dog object.
            'self' refers to the instance of the class (the object being created).
            'name' and 'age' are parameters passed when creating an object.
            """
            self.name = name  # Instance attribute
            self.age = age    # Instance attribute
            print(f"A new dog named {self.name} has been created!")

        def bark(self):
            """Simulate a dog barking."""
            print(f"{self.name} says Woof!")

        def get_age(self):
            """Return the dog's age."""
            return self.age

        def __str__(self):
            """Returns a user-friendly string representation of the object."""
            return f"Dog(Name: {self.name}, Age: {self.age})"

        def __repr__(self):
            """Returns an official string representation of the object (for developers)."""
            return f"Dog('{self.name}', {self.age})"

    print("\n--- Class Definition ---")
    print("Defined a 'Dog' class with name, age, and methods.")
    print("-" * 20)

    # 3. Creating Objects (Instantiating a Class)
    # An object is an instance of a class. When you create an object,
    # the __init__ method is automatically called.

    print("\n--- Creating Objects ---")
    my_dog = Dog("Buddy", 3)  # Creating an instance of Dog
    your_dog = Dog("Lucy", 5) # Creating another instance
    print("-" * 20)

    # 4. Accessing Attributes
    # You can access an object's attributes using dot notation.

    print("\n--- Accessing Attributes ---")
    print(f"My dog's name is {my_dog.name}.")
    print(f"My dog's age is {my_dog.age} years old.")
    print(f"Your dog's name is {your_dog.name}.")
    print(f"Your dog's age is {your_dog.age} years old.")

    # Accessing a class attribute
    print(f"All dogs are of species: {Dog.species}")
    print(f"Buddy's species: {my_dog.species}") # Can also access via instance
    print("-" * 20)

    # 5. Calling Methods
    # You can call an object's methods using dot notation.

    print("\n--- Calling Methods ---")
    my_dog.bark()
    your_dog.bark()
    print(f"Buddy is {my_dog.get_age()} years old.")
    print("-" * 20)

    # 6. Modifying Attributes
    # You can change the values of an object's attributes directly.

    print("\n--- Modifying Attributes ---")
    print(f"Before modification: {my_dog.name} is {my_dog.age} years old.")
    my_dog.age = 4
    print(f"After modification: {my_dog.name} is now {my_dog.age} years old.")
    print("-" * 20)

    # 7. __str__ and __repr__ Methods
    # These are special methods for providing string representations of objects.
    # __str__ is for human-readable output, __repr__ is for unambiguous output (often for developers).

    print("\n--- __str__ and __repr__ ---")
    print(f"print(my_dog) calls __str__: {my_dog}")
    print(f"repr(my_dog) calls __repr__: {repr(my_dog)}")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)