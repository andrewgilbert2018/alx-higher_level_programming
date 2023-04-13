#!/usr/bin/python3
'''
10-rectangle.py
a class Rectangle that inherits from Rectangle (9-rectangle.py)
add calculate area and size
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''calculate size and validate with integer validator'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
