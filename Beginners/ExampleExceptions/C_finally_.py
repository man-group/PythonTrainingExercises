#!/usr/bin/env python
"""Example of raising an exception where b() has a finally clause and a()
catches the exception.

Created on Aug 19, 2011

@author: paulross
"""

class ExceptionNormal(Exception):
    pass

class ExceptionCleanUp(Exception):
    pass

def a():
    try:
        b()
    except ExceptionNormal as err:
        print('  a(): CAUGHT "%s"' % err)
    
def b():
    try:
        c()
    finally:
        print('  b(): finally: This code is always executed.')

def c():
    print('Raising "ExceptionNormal" from c()')
    raise ExceptionNormal('ExceptionNormal raised from function c()')

def main():
    a()
    return 0

if __name__ == '__main__':
    main()
