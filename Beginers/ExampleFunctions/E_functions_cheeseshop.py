#!/usr/bin/env python
"""Does...

Created on Aug 25, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross.'

import pprint

#########################
# With keyword arguments.
#########################
def cheeseshop(kind, *args, **kwargs):
    print "-- Do you have any", kind, "?"
    print " *args ".center(40, '-')
    pprint.pprint(args)
    print " *args ".center(40, '-')
    print " *kwargs ".center(40, '-')
    pprint.pprint(kwargs)
    print " *kwargs ".center(40, '-')

def main():
    cheeseshop(
        "Limburger",
#         "It's very runny, sir.",
#         "It's really very, VERY runny, sir.",
        shopkeeper='Michael Palin',
        client="John Cleese",
        sketch="Cheese Shop Sketch")
    
if __name__ == '__main__':
    main()
#########################
# With keyword arguments.
#########################
