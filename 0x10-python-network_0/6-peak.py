#!/usr/bin/python3
"""
A python script that finds peaks
"""


def find_peak(list_of_integers):
    """
    A function that returns the peak of a list
    """
    length = len(list_of_integers) - 1

    if not list_of_integers:
        return None

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[length] > list_of_integers[length - 1]:
        return list_of_integers[length]

    for i in range(1, length):
        if list_of_integers[i] > list_of_integers[i + 1] and list_of_integers[i] > list_of_integers[i - 1]:
            return(list_of_integers[i])

    return None
