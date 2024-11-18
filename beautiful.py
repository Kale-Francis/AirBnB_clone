import math
import sys

class Circle:
    """
    A class to represent a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a given radius.

        Parameters:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius


def main():
    """
    Main function to create a Circle instance and print its area and circumference.
    """
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print(f"The area of the circle is: {circle.area():.2f}")
    print(f"The circumference of the circle is: {circle.circumference():.2f}")


if __name__ == "__main__":
    main()
