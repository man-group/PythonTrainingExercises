"""We have an existing dictionary that maps US states to their capitals.

Print the state capital of Idaho
Print all states.
Print all capitals.
Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'

Now we want to add the reverse look up, given the name of a capital what state
is it in?

Implement the function def get_state(capital): below so it returns the state.

GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

Created on 3 Mar 2015

@author: paulross
"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}

def capital_of_Idaho():
    return STATES_CAPITALS['Idaho']

def all_states():
    return STATES_CAPITALS.keys()

def all_capitals():
    return STATES_CAPITALS.values()

def states_capitals_string():
    l = []
    for k in sorted(STATES_CAPITALS.keys()):
        l.append('%s -> %s' % (k, STATES_CAPITALS[k]))
    return ', '.join(l)

# Pre-compute the reverse lookup, this is done a module import time
# What can go wrong here? - duplicates
CAPITALS_STATES = {v : k for k, v in STATES_CAPITALS.items()}

def get_state(capital):
    """A better solution in that we have pre-compute the reverse lookup and
    access that to get the capital. This will scale.
    We still do not have a good story for duplicate capital names however.
    """
    return CAPITALS_STATES[capital]


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
