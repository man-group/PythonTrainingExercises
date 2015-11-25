"""Given the text for Romeo and Juliet can you predict which actor is next to speak?

There is a fair amount of code here that I have prepared for you:
play.py is the play text itself.
result.py keeps track of how well your strategy works.
parser.py reads this into Python data structures.
romeo_and_juliet.py (this file) that you can modify.

Creating a strategy:
---------------------
main() will pass you a Play() object that contains the play contents. Your job
is to create a result.Result() object then iterate throught the acts and scenes.
For each scene, given the information that you have available pass your best
guess to the result.Result() object by calling guess(actor).
That will check and record whether your guess was a good one and returns the
actual actor who will speak next at this stage of the scene (None at the end
of the scene). You are free to use this information, but remember the scene
has moved on!

At the end of the play return your result and it will be printed out to see
how accurate you were:
 
Here is an example where we always guess 'ROMEO':

def strat_empty(play):
    ret_val = result.Result()
    for act in play.gen_acts():
        for scene in act.gen_scenes():
            ret_val.set_act_scene(act, scene)
            while True:
                #--------- Your code starts here ------
                # What are you going to choose?
                my_choice = 'ROMEO'
                #--------- Your code ends here ------
                actual_actor = ret_val.guess(my_choice)
                if actual_actor is None:
                    break
    return ret_val

This produces the following score:

Empty strategy (always ROMEO):
 Act Scene     Good      Bad Accuracy
   1     1     16.0     79.0     16.8%
   1     2     11.0     18.0     37.9%
   1     3      0.0     29.0      0.0%
   1     4     13.0     15.0     46.4%
   1     5     10.0     44.0     18.5%
   2     1      1.0      9.0     10.0%
   2     2     26.0     29.0     47.3%
   2     3      9.0     10.0     47.4%
   2     4     27.0     65.0     29.3%
   2     5      0.0     19.0      0.0%
   2     6      2.0      7.0     22.2%
   3     1     11.0     49.0     18.3%
   3     2      0.0     23.0      0.0%
   3     3     16.0     22.0     42.1%
   3     4      0.0      8.0      0.0%
   3     5      7.0     61.0     10.3%
   4     1      0.0     33.0      0.0%
   4     2      0.0     18.0      0.0%
   4     3      0.0      5.0      0.0%
   4     4      0.0     11.0      0.0%
   4     5      0.0     48.0      0.0%
   5     1      8.0      7.0     53.3%
   5     2      0.0      8.0      0.0%
   5     3      6.0     59.0      9.2%
              163.0    676.0     19.4%
              
Hmmm 19.4 %, can you do better?

There is one other example here which just guesses at random with predictably
poor results.

Maybe a strategy that guesses the last but one actor betting that the scene is
ROMEO/JULIET/ROMEO/JULIET/ROMEO/JULIET/ etc. Code it up!

Create your strategy by copying strat_empty(), rename it and add the call from
main(). Then add your strategy code where you see fit but don't alter the flow
of act/scene/actor or alter the lines that create result, initialise the result
for a new scene and passes your guess to the result.

Created on 18 Mar 2015

@author: paulross
"""
import random

from Exercises.RomeoAndJuliet.util import parser
from Exercises.RomeoAndJuliet.util import result
import MarkovChain

#----------------- Strategies ----------------

def strat_empty(play):
    """You can copy and modify this strategy."""
    ret_val = result.Result()
    for act in play.gen_acts():
        for scene in act.gen_scenes():
            ret_val.set_act_scene(act, scene)
            while True:
                #--------- Your code starts here ------
                # What are you going to choose?
                my_choice = 'ROMEO'
                #--------- Your code ends here ------
                actual_actor = ret_val.guess(my_choice)
                if actual_actor is None:
                    break
    return ret_val


def strat_random_all(play):
    """Just guess a random actor."""
    ret_val = result.Result()
    # Get all the actors, we are going to guess one randomly
    all_actors = play.dramatis_personae.keys()
    # Iterate through the acts
    for act in play.gen_acts():
        # Iterate through the scenes
        for scene in act.gen_scenes():
            # Prepare the results object for this act/scene
            ret_val.set_act_scene(act, scene)
            # Iterate through the actors in the scene
            while True:
                my_choice = random.choice(all_actors)
                actual_actor = ret_val.guess(my_choice)
                # If the actual actor is None it is the end of the scene
                if actual_actor is None:
                    break
    return ret_val

def strat_alternate_actors(play):
    """The next actor to speak is the one that spoke two goes ago.
    This works well for scenes with two actors that alternate."""
    ret_val = result.Result()
    # Iterate through the acts
    for act in play.gen_acts():
        # Iterate through the scenes
        for scene in act.gen_scenes():
            # Prepare the results object for this act/scene
            ret_val.set_act_scene(act, scene)
            # List of actors seen so far
            actors_seen = []
            # Iterate through the actors in the scene
            while True:
                # Make my choice of actor
                if len(actors_seen) > 1:
                    my_choice = actors_seen[-2]
                else:
                    # Can not guess unless two actors have spoken
                    my_choice = ''
                actual_actor = ret_val.guess(my_choice)
                # If the actual actor is None it is the end of the scene
                if actual_actor is None:
                    break
                else:
                    actors_seen.append(actual_actor)
    return ret_val

def strat_markov_chain(play):
    """You can copy and modify this strategy."""
    ret_val = result.Result()
    for act in play.gen_acts():
        for scene in act.gen_scenes():
            ret_val.set_act_scene(act, scene)
            mc = MarkovChain.MarkovChain()
            actors_seen = []
            while True:
                # Ask the markov chain for the most likely guess
                if len(actors_seen):
                    most_probable = mc.most_probable(actors_seen[-1])
                else:
                    most_probable = tuple()
                # If multiple values choose one randomly
                if len(most_probable) > 1:
                    my_choice = random.choice(most_probable)
                elif len(most_probable) == 1:
                    my_choice = most_probable[0]
                else:
                    # Not enough information
                    my_choice = ''
                actual_actor = ret_val.guess(my_choice)
                if actual_actor is None:
                    break
                else:
                    # Record the transition
                    if len(actors_seen):
                        mc.add(actors_seen[-1], actual_actor)
                    actors_seen.append(actual_actor) 
    return ret_val
        
def main():
    play = parser.get_play()
    print 'Empty strategy (always ROMEO):'
    result = strat_empty(play)
    print result
    print
    print 'Random in play:'
    result = strat_random_all(play)
    print result
    print
    print 'Alternating actors:'
    result = strat_alternate_actors(play)
    print result
    print
    print 'Markov chain:'
    result = strat_markov_chain(play)
    print result
    print


if __name__ == '__main__':
    main()
    print 'Bye, bye!'
