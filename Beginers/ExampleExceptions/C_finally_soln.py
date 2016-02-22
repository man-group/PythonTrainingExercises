#!/usr/bin/env python
"""Illustrates one possible solution to the problem where a finally block raises
an exception.

Created on Aug 19, 2011

@author: paulross
"""

class ExceptionNormal(Exception):
    pass

class ExceptionCleanUp(Exception):
    pass

def a():
    b()
    
def b():
    try:
        c()
    finally:
        # If doing something that might raise then trap this exception
        # to preserve the original one (if any).
        try:
            print('  b(): finally: This code is always executed.')
            cleanUp()
        except Exception as err:
            print('  -- HELP! Consuming: %s' % type(err))

def c():
    print('Raising "ExceptionNormal" from c()')
    raise ExceptionNormal('ExceptionNormal raised from function c()')

def cleanUp():
    raise ExceptionCleanUp('Can not clean up')
    
def main():
    a()
    return 0

if __name__ == '__main__':
    main()
