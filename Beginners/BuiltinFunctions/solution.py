"""Builtin functions problems.
It might be useful to browse here (adjust your version to suit):
https://docs.python.org/2.7/library/functions.html

1. Create the sequence [0, 3, 6, 9, ... N]. What is the problem if N is very large?
Is there a better way if N is very large?

2. Find the difference between the biggest and smallest values in the list
[4, 3, -9, 21, 0]

3. The same as 2. but use the absolute values in the list.

4.Convert a list:
['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
To a dictionary:
{
    0 : 'Zero',
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
}

5. I have two list a and b. Is there a way that I can tell if they are the same
list? For example in the following case they are the same list:
a = [1, 2, 3]
b = a
And any change to b be will be 'seen' by a.
However in this case a and b are not the same list in the sense that any change
to b be will NOT be 'seen' by a. 
a = [1, 2, 3]
b = [1, 2, 3]

Created on 22 Feb 2016

@author: paulross
"""
import sys

import pytest

def create_sequence(N):
    """Create the 3x table up to and including N."""
    return range(0, N + 3, 3)

def range_of_list():
    """Return the difference between the largest and smallest values in a list."""
    x = [4, 3, -9, 21, 0]
    return max(x) - min(x)

def range_of_list_abs():
    """Return the difference between the largest and smallest absolute values in a list."""
    x = [4, 3, -9, 21, 0]
    abs_x = [abs(value) for value in x]
    return max(abs_x) - min(abs_x)

def list_to_sequence_dict():
    """Create a dictionary where the key is the ordinal of the object in the list
    and the value is the object itself. For example: {0 : 'Zero', 1 : 'One', ...}"""
    x = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    d = {}
    for index, value in enumerate(x):
        d[index] = value
    return d

def is_same(a, b):
    """Return True is the two items are the same."""
    # This is the same as:
    # return a is b
    return id(a) == id(b)

#=========== Tests ===================
def test_create_sequence():
    assert create_sequence(12) == [0, 3, 6, 9, 12]
    
def test_range_of_list():
    assert range_of_list() == 30

def test_range_of_list_abs():
    assert range_of_list_abs() == 21

def test_list_to_sequence_dict():
    expected = {
        0 : 'Zero',
        1 : 'One',
        2 : 'Two',
        3 : 'Three',
        4 : 'Four',
        5 : 'Five',
        6 : 'Six',
        7 : 'Seven',
        8 : 'Eight',
        9 : 'Nine',
    }
    assert list_to_sequence_dict() == expected

def test_is_same():
    a = [1, 2, 3]
    b = a
    assert is_same(a, b)
    b = [1, 2, 3]
    assert not is_same(a, b)
    
def main():
    return pytest.main(__file__)

if __name__ == '__main__':
    sys.exit(main())
