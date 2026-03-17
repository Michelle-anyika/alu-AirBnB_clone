#!/usr/bin/python3
"""Module demonstrating PEP8-compliant Python code."""


class SampleClass:
    """A simple class to demonstrate clean and compliant code."""

    def __init__(self, name, age):
        """Initialize the sample class with name and age."""
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name}."

    def is_adult(self):
        """Check if the person is an adult."""
        return self.age >= 18


def calculate_sum(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    """Main function to demonstrate usage."""
    person = SampleClass("Michelle", 20)

    print(person.greet())
    print("Is adult:", person.is_adult())
    print("Sum:", calculate_sum(5, 3))


if __name__ == "__main__":
    main()
