"""With this string:
'monty pythons flying circus'

Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'

Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']

Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

Created on 3 Nov 2015

@author: paulross
"""
import pytest


def no_duplicates(a_string):
    # set(a_string) will remove duplicates
    # sorted(sequence) will create a sorted list of sequence
    # ''.join(sequence) will create a single string out of a sequence of strings
    # This can all be done in one line
    return ''.join(sorted(set(a_string)))


def reversed_words(a_string):
    # a_string.split() will create a list of words
    # reversed(sequence) will create a reversed sequence iterator
    # list(iterator) will iterate across the sequence and create a list of those objects
    # This can all be done in one line
    return list(reversed(a_string.split()))


def four_char_strings(a_string):
    # The key to this puzzle is to build it up in stages
    # Note that:
    # range(0,len(a_string),4)
    # Gives: [0, 4, 8, 12, 16, 20, 24]
    # And a_string[0:4]
    # Gives 'mont'
    # And a_string[4:8]
    # Gives 'y py'
    # And so on so a_string[i:i+4] seems useful
    # This can all be done in one line
    return [a_string[i:i+4] for i in range(0,len(a_string),4)]


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
