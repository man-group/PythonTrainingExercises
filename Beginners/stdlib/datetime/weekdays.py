"""Create a function that returns a list of a given size of date objects
that correspond to week days starting at a given date.

Created on 17 Feb 2016

@author: paulross
"""
import datetime

import pytest

def business_days(start_date, num):
    # Your code goes here
    pass


def test_business_days():
    start_date = datetime.date(2016, 1, 1)
    result = business_days(start_date, 10)
    expected = [
        datetime.date(2016, 1, 1),
        datetime.date(2016, 1, 4),
        datetime.date(2016, 1, 5),
        datetime.date(2016, 1, 6),
        datetime.date(2016, 1, 7),
        datetime.date(2016, 1, 8),
        datetime.date(2016, 1, 11),
        datetime.date(2016, 1, 12),
        datetime.date(2016, 1, 13),
        datetime.date(2016, 1, 14),
    ]
    assert result == expected


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
