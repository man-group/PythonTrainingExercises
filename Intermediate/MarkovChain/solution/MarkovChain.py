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
        # dict of {state_from : {state_to : count, ...}, ...}
        # Implemented as a dict of collections.Counter
        self._pairs = collections.defaultdict(collections.Counter)
    
    def add(self, state_from, state_to):
        """This adds a single observed occurrence of a state change from/to
        and returns None"""
        self._pairs[state_from][state_to] += 1
    
    def probability_table(self, state_from):
        """Return a dict of {state_to : probability, ...}.
        Returns empty dict if state_from unknown."""
        ret_val = {}
        try:
            counter = self._pairs[state_from]
            total = float(sum(counter.values()))
            ret_val = {k : v / total for k, v, in counter.items()}
        except KeyError:
            pass
        return ret_val
    
    def most_probable(self, state_from):
        """Returns a tuple of most probable next states."""
        ret_val = ()
        try:
            counter = self._pairs[state_from]
            if len(counter):
                max_val = max(counter.values())
                ret_val = tuple([k for k, v in counter.items() if v == max_val])
        except KeyError:
            pass
        return ret_val
