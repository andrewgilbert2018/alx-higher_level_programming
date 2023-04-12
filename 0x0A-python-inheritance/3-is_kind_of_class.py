#!/usr/bin/pytho3

'''
a function that returns True if the object is an
instance of, or if the object is an instance of a
class that inherited from,
the specified class ; otherwise False.
'''


def is_kind_of_class(objective, a_class):
    ''' Check instance of object and return true '''

    return (isinstance(objective, a_class))
