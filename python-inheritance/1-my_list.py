#!/usr/bin/python3
"""
This script defines a class "MyList" that inherits from the built-in
"list" class and adds a method to print the list in ascending order.

Methods:
    print_sorted(): Print the list in ascending order.
"""


class MyList(list):
    """
    "MyList" is a class that inherite from the class "list" and add
    a method to print the list in the ascending order.

    Method:
        print_sorted(): Print the list in the ascending order.
    """

    def print_sorted(self):
        """ Display the sorted list in ascending order """
        print(sorted(self))
