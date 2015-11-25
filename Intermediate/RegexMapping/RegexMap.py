#!/usr/bin/env python
"""The task is to parse a list of lines and use regular expressions to process
them differently according to what they contain.
If the line is all digits we want to convert that to an integer and divide it
by 2, if it is all non-digits then change it lower case otherwise represent it
with None.

For example, these lines:
288
ABCDEFGH
1A2B3C4D

Hello world
42

Will be converted to the list: [144, 'abcdefgh', None, None, 'hello world', 21]

The regular expression pattern for digits is \d and non-digits is \D.

Created on Sep 21, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import re

def matchLines(theLineS):
    """Given a list of lines return a list of objects:
    If the line is all digits then divide it by 2.
    If the line is all non-digits then make it lower case.
    Other lines are represented by None."""
    result = []
    for l in theLineS:
        # Your code goes here
        pass
    return result

def main():
    text = """288
ABCDEFGH
1A2B3C4D

Hello world
42"""
    result = matchLines(text.split('\n'))
    print result

if __name__ == '__main__':
    main()
