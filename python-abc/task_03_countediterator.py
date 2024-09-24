#!/usr/bin/env python3
"""
A custom iterator that counts the number of iterations.
"""


class CountedIterator:
    def __init__(self, iterable, counter=0):
        """
        Initializes the CountedIterator with an iterable and a counter.
        """
        # iter(arg) transforme l'arg en iterable
        self.iter = iter(iterable)
        self.counter = counter

    def get_count(self):
        """
        Returns the current iteration count.
        """
        return self.counter

    def __next__(self):
        """
        Returns the next item from the iterable and increments the counter.
        Else raise StopIteration.
        """
        try:
            # next() obtiens le prochain élément d'un itérable
            item = next(self.iter)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
