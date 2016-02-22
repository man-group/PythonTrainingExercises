#!/usr/bin/env python
"""Illustrates the problem where a finally block raises an exception. This
can mask the original exception that caused the problem in the first place.

The user sees the ExceptionCleanUp but not the ExceptionNormal which was masked
(in Python 2.x). Python 3 reports both exceptions.

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
        print('  b(): finally: This code is always executed.')
        cleanUp()

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
