#!/usr/bin/python3
"""class BaseGeometry that raise an Exception message"""


class BaseGeometry():
    """
    A class to represent basic geometric shapes.

    Methods
    -------
    area():
        Raises an Exception indicating that the area method is not implemented.
    """
    def area(self):
        """
        Public method that raise an Exception

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")
