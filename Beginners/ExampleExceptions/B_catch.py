#!/usr/bin/env python
"""Example of raising an exception through a call chain.
Function c() will randomly raise a type ExceptionOne or ExceptionTwo. These
will be caught by a() and b() respectively.

Created on Aug 19, 2011

@author: paulross
"""

import random

class ExceptionOne(Exception):
    pass

class ExceptionTwo(Exception):
    pass

def a():
    try:
        b()
        print('  a() called b() with no exception raised')
    except ExceptionOne as err:
        print('  a() CAUGHT %s' % err)
    
def b():
    try:
        c()
    except ExceptionTwo as err:
        print('  b() CAUGHT %s' % err)
    else:
        print('  b() No exception raised')

def c():
    # randVal is (0, 1, 2)
    randVal = random.randint(0, 2)
    if randVal == 1:
        raise ExceptionOne('I am the One')
    elif randVal == 2:
        raise ExceptionTwo('I am the One two')
    # Do something. Hopefully its useful.

def main():
    for i in range(8):
        print('Round %d:' % i)
        a()
    return 0

if __name__ == '__main__':
    main()
