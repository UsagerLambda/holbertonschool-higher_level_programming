#!/usr/bin/python3

"""
This module defines a class named Rectangle.

The Rectangle class represents a rectangle with a specified width and height.
It includes methods to get and set these dimensions, ensuring that they are
non-negative integers.

The class includes the following methods:
    - __init__(self, width=0, height=0): Initializes the rectangle
    with the given width and height.
    - width(self): Getter for the width property.
    - width(self, value): Setter for the width property.
    - height(self): Getter for the height property.
    - height(self, value): Setter for the height property.
"""


class Rectangle():
    """
    A class used to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Return the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, ensuring it is a non-negative integer.

        Args:
            value (int): The width of the rectangle

        Raises:
            TypeError: If width is not a integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle,
        ensuring it is a non-negative integer.

        Args:
            value (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns: float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns: float: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        If either the width or the height is 0, returns an empty string.
        Convert print_symbol into a string.
        Otherwise, returns a string representation of the rectangle,
        where each line is filled with the '#' character, with the number
        of lines corresponding to the height and the number of '#' characters
        in each line corresponding to the width.

        Returns:
        str: A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)  # Convertie print_symbol en strings
        rectangle_lines = []
        for _ in range(self.height):
            rectangle_lines.append(symbol * self.width)
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate a new instance with the same values.

        The string returned is in the form 'Rectangle(height, width)'
        where 'height' and 'width' are the dimensions of the rectangle.

        Returns:
            str: A string that represents the rectangle in a way that
            can be used to recreate it using eval().
        """
        if self.height > self.width:
            return "Rectangle({}, {})".format(self.width, self.height)
        if self.height < self.width:
            return "Rectangle({}, {})".format(self.height, self.width)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.

        This method is called when the rectangle instance is about to be
        destroyed.
        It prints 'Bye rectangle...' to notify that the object
        has been deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles to determine which has the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area.
            If the areas are equal, returns rect_1.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # 'instance'.area() appelle la méthode area()
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new square with the specified size.

        Args:
            size (int, optional): The size of the sides of the square.
            Default is 0.

        Returns:
            Rectangle: An instance of Rectangle
            where both height and width are equal to size.
        """
        return Rectangle(size, size)
