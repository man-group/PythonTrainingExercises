#!/usr/bin/env python
"""Does...

Created on Aug 25, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross.'

###################################
# The many ways of calling parrot()
###################################
def parrot(voltage,
           state='a stiff',
           action='voom',
           type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

def main():
    parrot(1000)
    print
    parrot(action='VOOOOOM', voltage=1000000)
    print
    parrot('a thousand', state='pushing up the daisies')
    print
    parrot('a million', 'bereft of life', 'jump')
    print
    # These will raise a SyntaxError
#    parrot()                     # required argument missing
#    parrot(voltage=5.0, 'dead')  # non-keyword argument following keyword
    parrot(110, 'a', 'b', voltage=220)     # duplicate value for argument
#    parrot(actor='John Cleese')  # unknown keyword

if __name__ == '__main__':
    main()
    
########################################
# END: The many ways of calling parrot()
########################################
