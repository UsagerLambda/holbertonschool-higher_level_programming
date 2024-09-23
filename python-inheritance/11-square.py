#!/usr/bin/python3
"""
Module defining the BaseGeometry class
for basic geometric shape operations.
"""


class BaseGeometry:
    """
    A class to represent basic geometric shapes.

    Methods
    -------
    area():
        Raises an Exception indicating that the area method is not implemented.

    interger_validator(name: str, value, int)
        Validate that value is a positive integer, if not raise an Exception
    """
    def area(self):
        """
        Public method that raise an Exception

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Parameters:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new rectangle
        with the specified width and height.
        area(): Calculates and returns the area of the rectangle.
        __str__(): Returns a string representation of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with a specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle in the format
            '[Rectangle] width/height'.
        """
        return '[{}] {}/{}'.format(__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            str: The area of the rectangle as a string.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The length of a side of the square.
            Must be a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        # super() appelle __init__ de la classe parent (Rectangle)
        # et lui donne size pour width & height
        super().__init__(size, size)

    def area(self):
        """
        Call the function area from the parent class

        Returns:
            The area of the square.
        """
        return super().area()

    def __str__(self):
        """
        Return a string representation of the object.

        This method returns a formatted string in the following format:
        "[ClassName] size / size", where:
        - ClassName is the name of the class
        (retrieved using self.__class__.__name__)
        - size is the value of the __size attribute of the object.

        Returns:
        str: A formatted string representing the object.
        """
        return f"[{self.__class__.__name__}] {self.__size} / {self.__size}"
