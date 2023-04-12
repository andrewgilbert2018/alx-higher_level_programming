#!/usr/bin/python3

'''
a function that writes a string to a text file (UTF8) and returns the number of characters written
'''


def write_file(nameoffile="", text=""):
    ''' Function that writes string to a text file UTF8
    Args:
        nameofname: filename
        text: string write to text
    Raises
        Exception: when the file can be opened
    '''

    with open(nameoffile, 'n', encoding="utf-8") as b:
        return b.write(text)
