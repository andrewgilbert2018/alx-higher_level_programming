#!/usr/bin/python3
'''
 function that reads a text file (UTF8) and prints it to stdout
'''


def read_file(nameoffile=""):
    '''This defined function read_file reads utf8 text file'''
    with open(nameoffile, encoding='UTF-8') as n:
        for line in n:
            print(line, end='')
