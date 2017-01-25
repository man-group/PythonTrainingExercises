#!/usr/bin/env python
"""Task create a class to represent lengths.

Create a specialised exception that this module might raise on error.

This needs to define an __init__() constructor that takes a a number,
assumed to be meters

Implement __str__ to give a string representation used by str() and print

Implement a function, convert(string) that returns the value converted to 'feet', 'mm', 'inch'

Implement a function to add two classes together and return the sum as a class

STRETCH: Change the constructor so it can take a number and a string, for
example:
l = Length(21.2, "inch")
STRETCH: Change the function that adds two classes together to be more flexible
so that it can add a number to a class Length returning a class Length.
Example:
l = Length(23)
m = l + 21


Created on Sep 12, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import sys

import pytest

# Create a specialise exception that we can use on error.
class ExceptionLength(Exception):
    pass

class Length(object):
    """Class that represents length. Constructor takes a number represents
    metres."""
    CONVERSION_FACTOR = {
        'feet'  : 1 / 0.3048,
        'inch'  : 1000 / 25.4,
        'mm'    : 1000,
    }
    
    def __init__(self, theValue):
        # theValue is in metres.
        self.value = theValue
        
    def __str__(self):
        return 'Length: {0:.3f} (m)'.format(self.value)
    
    def convert(self, uom):
        """Returns the value in the specified units of measure."""
        try:
            return self.value * Length.CONVERSION_FACTOR[uom]
        except KeyError:
            raise ExceptionLength('Can not convert to: {0:s}'.format(str(uom)))
        
    def __add__(self, other):
        """Return a new instance of two classes added together."""
        return Length(self.value + other.value)


def test_convert():
    length = Length(12)
    assert 12000 == length.convert('mm')


def test_str():
    length = Length(12.5)
    assert 'Length: 12.500 (m)' == str(length)


def test_convert_raises():
    length = Length(12.5)
    with pytest.raises(ExceptionLength) as err:
        length.convert('miles')
    assert 'Can not convert to: miles' == err.value.message


def test_add():
    len_a = Length(2)
    len_b = Length(6)
    len_total = len_a + len_b
    assert 8 == len_total.value


def main():
    return pytest.main(__file__)

if __name__ == '__main__':
    sys.exit(main())

