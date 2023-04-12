#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """ Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
