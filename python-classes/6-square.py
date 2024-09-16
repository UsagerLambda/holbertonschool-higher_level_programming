#!/usr/bin/python3

"""
Class square with private instance attribute 'size'

In def __init__
We check if size is a integer and not < 0

In def area
We return the area of the square

"""


class Square():
    """
    Class that defines a square with a specific size and position.

    Attributes:
        size (int): Size of the square (default is 0).
        position (tuple): A tuple of two integers specifying the position
        for printing the square (default is (0, 0)).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a specific size and position.

        Args:
        size (int): The size of the square (must be >= 0).
        position (tuple): A tuple of two positive integers for the position.
        """
        self.__size = size  # Private Attribute ("__")
        self.__position = position  # Private Attribute ("__")
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square

        Args:
        value (int): The new size for the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
            tuple: A tuple of 2 positive integers specifying the position
                where the square should be printed.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers
            indicating the position.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):  # Vérifie si value est un tuple
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:  # Vérifie que le tuple contient bien 2 éléments
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            # Vérifie que chaque élément du tuple est un entier et >= 0
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Assigne la valeur à l'attribut privé

    def my_print(self):
        """
        Prints the square using the character '#'.

        If the size is 0, it prints a blank line.
        The square is printed with the specified position,
        where the first value of the position tuple defines
        the horizontal indentation, and the second value defines
        the number of blank lines before the square.
        """
        if self.__size != 0:
            if self.position[1] > 0:
                for _ in range(self.position[1]):
                    print()

            for i in range(self.__size):
                print(' ' * self.position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
