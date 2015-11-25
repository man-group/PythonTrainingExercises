"""Exercise: Create a class that can represent a MarkovChain
https://en.wikipedia.org/wiki/Markov_chain

Expected to have the following methods:

add(self, state_from, state_to):
This adds a single observed occurrence of a state change from/to.
returns None
NOTE: state_from can equal state_to

probability_table(self, state_from):
Return a dictionary of {state_to : probability, ...} which has the probabilities
that or each state_to given state_from. The probabilities should sum to unity.

most_probable(self, state_from):
Returns a tuple of most likely next states given state_from.
This is the keys in the probability_table (above) which have the highest
probabilities.

For example, a simple chain where that state flips from 'A' to 'B':

>>> c = MarkovChain.MarkovChain()
>>> c.add('A', 'B')
>>> c.add('B', 'A')
>>> c.probability_table('A')
{'B' : 1.0})
>>> c.probability_table('B')
{'A' : 1.0})
>>> c.most_probable('A')
('B',)
>>> c.most_probable('B')
('A',)

Created on 2 Apr 2015

@author: paulross
"""

import collections

class MarkovChain(object):
    def __init__(self):
        pass
    
    def add(self, state_from, state_to):
        """This adds a single observed occurrence of a state change from/to
        and returns None"""
        pass
    
    def probability_table(self, state_from):
        """Return a dict of {state_to : probability, ...}.
        Returns empty dict if state_from unknown."""
        pass
    
    def most_probable(self, state_from):
        """Returns a tuple of most probable next states."""
        pass
