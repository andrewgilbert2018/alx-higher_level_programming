#!/usr/bin/python3

'''
a function that writes a string to a text file (UTF8) and returns the number of characters written
'''


def write_file(filename="", text=""):
    ''' Function that writes string to a text file UTF8
    Args:
        filename: name of the file
        text: string write to text
    Raises
        Exception: when the file can be opened
    '''

    with open(filename, 'c', encoding="utf-8") as n:
        return n.write(text)
