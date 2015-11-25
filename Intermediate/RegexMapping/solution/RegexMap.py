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

Notes on This Solution
----------------------
One way to do this is to put an if statement in matchLines() that checks each
match then takes the appropriate action. This works fine for simple jobs but
rapidly becomes unwieldy when additional requirements are added (there is one
job in AHL that uses 50 to 80 regular expressions!).

The approach here is to have a table (RE_OPTIONS) which contains pairs of
regular expressions and functions. If the regular expression matches then the
function is called with the match object and the return value added to the
result. The advantage is that if a new kind of match is needed then you just
add a function to handle the match and an entry in the table with the
regular expression and function name. No other code has to be changed. 


Created on Sep 21, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import re

def digits(m):
    """Takes a match object, one that matches digits."""
    assert(m is not None)
    return int(m.group(1)) / 2


def letters(m):
    """Takes a match object, one that matches non-digits."""
    assert(m is not None)
    return m.group(1).lower()


RE_OPTIONS = (
    (re.compile(r'^(\d+)$'), digits),
    (re.compile(r'^(\D+)$'), letters),
)


def matchLines(theLineS):
    """Given a list of lines return a list of objects:
    If the line is all digits then divide it by 2.
    If the line is all non-digits then make it lower case.
    Other lines are represented by None."""
    result = []
    for l in theLineS:
        for patt, func in RE_OPTIONS:
            m = patt.match(l)
            if m is not None:
                result.append(func(m))
                break
        else:
            result.append(None)
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
