#!/usr/bin/env python3


class SwimMixin:
    """Mixin class that adds swimming functionality."""

    def swim(self):
        """Makes the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying functionality."""

    def fly(self):
        """Makes the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly."""

    def roar(self):
        """Makes the dragon roar."""
        print("The dragon roars")
