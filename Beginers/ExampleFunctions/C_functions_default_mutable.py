#!/usr/bin/env python
"""Does...

Created on Aug 25, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross.'

################################
# Problem with mutable defaults.
################################
def defaultMutableCatch(a=[1,]):
    a.append('Ooops')
    return a

x = [1,]

def defaultMutableFix(a=x):
    if a is None:
        a = []
    a.append('Ooops')
    return a

def main():
    # defaultMutableCatch()
    print 'defaultMutableCatch():', defaultMutableCatch()
    print 'defaultMutableCatch():', defaultMutableCatch([])
    print 'defaultMutableCatch():', defaultMutableCatch()
    # defaultMutableFix()
    print 'defaultMutableFix():', defaultMutableFix()
    print 'defaultMutableFix():', defaultMutableFix()
    print 'defaultMutableFix():', defaultMutableFix()
    
if __name__ == '__main__':
    main()
#####################################
# END: Problem with mutable defaults.
#####################################
