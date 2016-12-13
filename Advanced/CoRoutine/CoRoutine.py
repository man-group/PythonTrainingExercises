#!/usr/bin/env python
"""Write a co-routine that is sent words and maintains a sorted list of them.

This generator can be used in the following way:

g = keep_sorted()
# Start the generator
g.next()
# Send stuff
g.send('zzz')
g.send('Hi there')
# Use next to retrieve the list
print 'Sorted list is {0:s}'.format(g.next())    
g.close()

Created on Sep 12, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-09-12'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

def keep_sorted():
    """A co-routine that receives words and maintains a sorted list of them.
    """ 
    l = []
    while True:
        # Your code goes here
        yield l


if __name__ == '__main__':
    g = keep_sorted()
    # Start the generator
    g.next()
    # Send stuff
    print g.send('zzz')
    print g.send('Hi there')
    print 'Sorted list is {0:s}'.format(g.next())    
    g.close()
