#!/usr/bin/env python
"""Illustrates Python function keyword arguments packing and unpacking.

Created on Aug 25, 2011

@author: paulross
"""

def unpackKwargs(**kwargs):
    keys = kwargs.keys()
    keys.sort()
    for kw in keys:
        print kw, ":", kwargs[kw]

def main():
    print 'callUnpackKwargs():'
    print 'Specific arguments:'
    unpackKwargs(name='python', version=2.6)
    d = {
        'name' : 'python',
        'version' : 2.6,
    }
    print
    print 'Unpacked arguments:'
    unpackKwargs(**d)

if __name__ == '__main__':
    main()
