#!/usr/bin/env python
"""Does...

Created on Aug 25, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross.'


##################################
# Simple functions, with defaults.
##################################
def twoArgsOneDefault(a, b='default_value'):
    print '    a=%s, b=%s' % (a, b)
    
def main():
    print 'callTwoArgsOneDefault():'
    twoArgsOneDefault('a_only')
    twoArgsOneDefault('a_value', b='b_given')

if __name__ == '__main__':
    main()

## Having positional arguments after a default is a syntax error
#def twoArgsOneDefaultWrong(a='something', b):
#    print 'a=%s, b=%s' % (a, b)

#######################################
# END: Simple functions, with defaults.
#######################################
