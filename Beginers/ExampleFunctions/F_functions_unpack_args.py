#!/usr/bin/env python
"""Illustrates Python function arguments packing and unpacking.

Created on Aug 25, 2011

@author: paulross
"""

def unpackArgs(*args):
    for arg in args:
        print type(arg), arg
    print

def main():
    print 'callUnpackArgs():'
    print 'Specific arguments:'
    unpackArgs(0,1,2,3)
    l = ['a', 'b', 'c', 'd']
    print 'Single list argument:'
    unpackArgs(l)
    print 'Unpacked list argument:'
    unpackArgs(*l)
    print 'Single value unpacked'
    unpackArgs(*'hello')

if __name__ == '__main__':
    main()
