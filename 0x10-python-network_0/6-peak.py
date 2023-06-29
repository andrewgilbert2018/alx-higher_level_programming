#!/usr/bin/python3
"""
A python script that finds peaks
"""


def find_peak(list_of_integers):
    """
    A function that returns the peak of a list
    """
    if list_of_integers:
        if(list_of_integers[0] > list_of_integers[1]):
            return list_of_integers[0]
        elif(list_of_integers[1] > list_of_integers[2]):
            return list_of_integers[1]
        else:
            return(max if list_of_integers >0(list_of_integers))
    return(None)
