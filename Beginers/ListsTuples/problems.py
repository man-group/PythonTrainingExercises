"""Some exercises involving lists.

transpose()
===========
Create a function that takes a list of lists and returns the transpose. So given:
[
    [1, 2, 3],
    ['A', 'B', 'C'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
    [3, 'C'],
]

In the case of uneven length lists choose then truncate to the shortest, so given:
[
    [1, 2, 3],
    ['A', 'B'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
]

Hint: There is a builtin function that can help you.

peak_to_peak()
==============
Create a function that returns the peak-to-peak value of the values in a list.

Hint: There are a couple of builtin functions that can help you.

Challenges: What to do when the list is empty?
If the list contains non-numeric values?

list rotation
=============
Rotate a list by taking the value from one end a putting it on the other end.
Create two functions rotate_left() and rotate_right() that modify a list in
place as follows, given the list ['A', 'B', 'C']:

rotate_left() changes it to ['B', 'C', 'A']
rotate_right() changes it to ['C', 'A', 'B']

More: The solution has two failing tests, fix the solution so that the tests pass.

Created on 21 Feb 2016

@author: paulross
"""
import pytest

def transpose(list_of_lists):
    """Transpose a list of lists."""
    # Your code goes here
    pass

def peak_to_peak(alist):
    """Return the peak to peak value of a list."""
    pass

def rotate_left(alist):
    """Rotates a list to the left so that the first item appears at the end."""
    pass

def rotate_right(alist):
    """Rotates a list to the right so that the last item appears at the beginning."""
    pass

#=================== Tests ========================
def test_transpose():
    data = [
        [1, 2, 3],
        ['A', 'B', 'C'],
    ]
    expected = [
        [1, 'A'],
        [2, 'B'],
        [3, 'C'],
    ]
    assert transpose(data) == expected

def test_transpose_non_equal_length():
    data = [
        [1, 2, 3],
        ['A', 'B'],
    ]
    expected = [
        [1, 'A'],
        [2, 'B'],
    ]
    assert transpose(data) == expected

def test_peak_to_peak():
    assert peak_to_peak([1, 8]) == 7
    assert peak_to_peak([-1, -8]) == 7
    assert peak_to_peak([9, -8]) == 17

def test_rotate_left():
    l = ['A', 'B', 'C']
    rotate_left(l)
    assert l ==  ['B', 'C', 'A']

def test_rotate_right():
    l = ['A', 'B', 'C']
    rotate_right(l)
    assert l == ['C', 'A', 'B']

def test_rotate_left_empty():
    l = []
    rotate_left(l)
    assert l == []

def test_rotate_right_empty():
    l = []
    rotate_right(l)
    assert l == []

def main():
    return pytest.main(__file__)

if __name__ == '__main__':
    main()
