#!/usr/bin/env python
"""Examples of Python functions.

Created on Aug 25, 2011

@author: paulross
"""

###################
# Simple functions.
###################
def noArgs():
    """Function that takes no arguments."""
    print '    noArgs(): No arguments'

def twoArgs(a, b):
    """Function that takes two arguments."""
    print '    twoArgs(): a=%s, b=%s' % (a, b)

def main():
    print 'callSimple():'
    noArgs()
    twoArgs(12, 34)
    twoArgs(b='b_given', a='a_given')

if __name__ == '__main__':
    main()
########################
# END: Simple functions.
########################
