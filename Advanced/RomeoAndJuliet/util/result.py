"""
Created on 19 Mar 2015

@author: paulross
"""

class Result(object):
    """Class that tallies the results of guessing the actor."""
    def __init__(self):
        self._result = {}
        self._act = None
        self._scene = None
        self._actor_gen = None
        self._good = 0
        self._bad = 0
        
    def add(self, act, scene, good, bad):
        if act not in self._result:
            self._result[act] = {}
        self._result[act][scene] = (good, bad)
    
    def set_act_scene(self, act_object, scene_object):
        self._act = act_object.act_num
        self._scene = scene_object.scene_num
        self._actor_gen = scene_object.gen_actors()
        self._good = 0
        self._bad = 0
        
    def guess(self, guessed_actor):
        try:
            actual_actor = next(self._actor_gen)
            if actual_actor == guessed_actor:
                self._good += 1
            else:
                self._bad += 1
            return actual_actor
        except StopIteration:
            # End of scene
            self.add(self._act, self._scene, self._good, self._bad)
    
    def __str__(self):
        lines = []
        lines.append('%4s %5s %8s %8s %8s' 
                     % ('Act', 'Scene', 'Good', 'Bad', 'Accuracy'))
        tot_good = tot_bad = 0
        for act in sorted(self._result.keys()):
            for scene in sorted(self._result[act].keys()):
                good = self._result[act][scene][0]
                bad = self._result[act][scene][1]
                lines.append('%4s %5s %8.1f %8.1f %8.1f%%' 
                             % (act, scene, good, bad, 100.0 * good / (good + bad)))
                tot_good += good
                tot_bad += bad
        lines.append('%4s %5s %8.1f %8.1f %8.1f%%' 
                     % ('', '', tot_good, tot_bad,
                        100.0 * tot_good / (tot_good + tot_bad)))
        return '\n'.join(lines)
