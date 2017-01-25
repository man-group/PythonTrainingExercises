"""
Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number
"""

def what_sign(n):
    if n > 0:
        return 'Positive'
    elif n < 0:
        return 'Negative'
    else:
        return 'Zero'


def test_what_sign():
    assert what_sign(3) == 'Positive'
    assert what_sign(0) == 'Zero'
    assert what_sign(-3) == 'Negative'

"""
Write a function 'fizzbuzz' that prints the integers from 1 to 100.

But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

def fizzbuzz():
    for num in range(1,101):
        msg = ''
        if num % 3 == 0:
            msg += 'Fizz'
        if num % 5 == 0:
            msg += 'Buzz'
        else:
            msg = str(num)
        print msg

"""
Write a function 'remove_indices' which removes one or more indicies from a list.

For example given the list:
["John", "Bob", "Charles", "Trev"]
and the indices:
[1, 2]
the resulting list will be:
["John", "Trev"]
"""


def remove_indices(mylist, idxs):
    result = []
    for i, l in enumerate(mylist):
        if i not in idxs:
            result.append(l)
    return result


def test_remove_indices():
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [0]) == ["Bob", "Charles", "Trev"]
    assert remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2]) == ["John", "Trev"]


""""
Modify connect to handle failed connections
"""
import random


def open_connection():
    if random.randint(0, 3) != 0:
        raise ValueError('failed to connect')
    return True


def connect(nretry=100):
    for _ in range(nretry):
        try:
            if open_connection():
                return True
        except ValueError:
            continue
    return False

def test_connect():
    for _i in range(100):
        assert connect()
