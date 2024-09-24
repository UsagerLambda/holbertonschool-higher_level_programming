#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [item] to the list.")

    def extend(self, iterable):
        super().extend(iterable)

    def remove(self, item):
        super().remove(item)

    def pop(self):
        pass
