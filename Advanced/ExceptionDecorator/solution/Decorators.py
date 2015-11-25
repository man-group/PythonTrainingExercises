#!/usr/bin/env python
"""Write a decorator that makes sure that only a particular type of exception is
raised by the function.
The trick here is to catch all exceptions then if any exception is raised
convert it to the type of exception that we want to raise.

Complete the decorator raises() below.

Created on Sep 21, 2011

@author: paulross
"""

__author__  = 'Paul Ross'
__date__    = '2011-08-03'
__version__ = '0.1.0'
__rights__  = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import functools

def raises(exception_cls):
    """Wraps a function ensuring only one type of exception is raises."""
    def wrap(fnIN, *args,**kwargs):
        @functools.wraps(fnIN)
        def wrap_func(*args, **kwargs):
            """Wrapping function with exception translation."""
            # Save and delete the following line and use it in your own code
            # fnIN(*args,**kwargs)
            try:
                return fnIN(*args,**kwargs)
            except Exception as err:
                raise exception_cls(str(err))
        return wrap_func 
    return wrap

# Right and wrong exceptions
class RightException(Exception): pass
class WrongException(Exception): pass


@raises(RightException)
def functionOne():
    """Documentation for functionOne, this may raise an WrongException."""
    raise WrongException('Raising an WrongException (originally)')


def main():
    try:
        functionOne()
    except RightException as err:
        print('Success! caught an RightException exception: "{0:s}"'.format(str(err)))
    except WrongException as err:
        print('FAILURE! caught an WrongException exception: "{0:s}"'.format(str(err)))

if __name__ == '__main__':
    main()
