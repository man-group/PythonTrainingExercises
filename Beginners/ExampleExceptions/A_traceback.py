#!/usr/bin/env python
"""Example of raising an exception through a call chain.

Created on Aug 19, 2011

@author: paulross
"""

def a():
    b()
    
def b():
    c()

def c():
    raise Exception('Ouch')

def main():
    a()
    
if __name__ == '__main__':
    main()
