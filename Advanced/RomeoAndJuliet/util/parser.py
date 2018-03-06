"""Parser for Romeo and Juliet.

Created on 18 Mar 2015

@author: paulross
"""
from Exercises.RomeoAndJuliet.util import play

def _is_stage_direction(line):
    """Returns True if the line is a stage direction."""
    line = line.strip()
    return line.startswith('[') and line.endswith(']')

def get_scenes():
    """Returns a list of scenes where each scene is a list of pairs:
    [(line_number, actor), ...] """
    scenes = []
    scene = []
    for line_num, line in enumerate(play.PLAY_TEXT.split('\n')):
        words = line.split()
        actor = None
        if len(words):
            if len(words) and words[0] in play.DRAMATIS_PERSONAE:
                actor = words[0]
            elif len(words) > 1 and ' '.join(words[:2]) in play.DRAMATIS_PERSONAE:
                actor = ' '.join(words[:2])
            elif words[0] == 'SCENE':
                if len(scene):
                    scenes.append(scene)
                scene = []
        if actor is not None:
            scene.append((line_num, actor))
    return scenes

class Play(object):
    """Represents the complete play."""
    def __init__(self, name):
        self.name = name
        self._acts = []
        # dict of {name : description, ...}
        self.dramatis_personae = play.DRAMATIS_PERSONAE

    def __getattribute__(self, item, internal_ref=False):
        if internal_ref or item != '_acts':
            return super(Play, self).__getattribute__(item)

        raise AttributeError("You're not allowed to access the `_acts` list.")

    def add_act(self, act):
        acts = self.__getattribute__('_acts', internal_ref=True)
        acts.append(act)

    def gen_acts(self):
        acts = self.__getattribute__('_acts', internal_ref=True)
        for act in acts:
            yield act

    def __str__(self):
        lines = ['Play: %s' % self.name]
        for act in self._acts:
            lines.append('%s\n' % str(act))
        return '\n'.join(lines)


class Act(object):
    """Represents an act in the play."""
    def __init__(self, act_num):
        self.act_num = act_num
        self._scenes = []

    def __getattribute__(self, item, internal_ref=False):
        if internal_ref or item != '_scenes':
            return super(Act, self).__getattribute__(item)

        raise AttributeError("You're not allowed to access the `_scenes` list.")

    def add_scene(self, scene):
        scenes = self.__getattribute__('_scenes', internal_ref=True)
        scenes.append(scene)

    def gen_scenes(self):
        scenes = self.__getattribute__('_scenes', internal_ref=True)
        for scene in scenes:
            yield scene

    def __str__(self):
        lines = ['Act %d' % self.act_num]
        for scene in self._scenes:
            lines.append('  %s' % str(scene))
        return '\n'.join(lines)


class Scene(object):
    """Represents a scene in an act. This contains the ordered list of actor names."""
    def __init__(self, scene_num):
        self._index = 0
        self.scene_num = scene_num
        self._actors = []

    def __getattribute__(self, item, internal_ref=False):
        if internal_ref or item != '_actors':
            return super(Scene, self).__getattribute__(item)

        raise AttributeError("You're not allowed to access the `_actors` list.")

    def add_actor(self, actor):
        actors = self.__getattribute__('_actors', internal_ref=True)
        actors.append(actor)

    def gen_actors(self):
        actors = self.__getattribute__('_actors', internal_ref=True)
        for actor in actors:
            yield actor

    def __str__(self):
        return 'Scene %d, actors: %s' % (self.scene_num, ', '.join(self._actors))


def get_play():
    """Returns a Play object that has acts, scenes and actors names in speaking order.
    """
    play = Play('Romeo and Juliet')
    d = get_acts_scenes_actors()
    for act_num in sorted(d.keys()):
        act = Act(act_num)
        for scene_num in sorted(d[act_num].keys()):
            scene = Scene(scene_num)
            for actor in d[act_num][scene_num]:
                scene.add_actor(actor)
            act.add_scene(scene)
        play.add_act(act)
    return play

def get_acts_scenes_actors():
    """Returns a dict of acts, scenes and actor names:
    {act : {scene : [actors, ...], ...}, ...}
    act and scene are integers
    """
    ret_val = {}
    act = None
    act_num = scene_num = 0
    actors = []
    for line in play.PLAY_TEXT.split('\n'):
        words = line.split()
        if len(words):
            if len(words) and words[0] in play.DRAMATIS_PERSONAE:
                actors.append(words[0])
            elif len(words) > 1 and ' '.join(words[:2]) in play.DRAMATIS_PERSONAE:
                actors.append(' '.join(words[:2]))
            elif len(words) > 1 and words[0] == 'ACT' and words[1] != act:
                if len(actors):
                    ret_val[act_num][scene_num] = actors
                    actors = []
                act_num += 1
                ret_val[act_num] = {}
                scene_num = 0
                act = words[1]
            elif act is not None and words[0] == 'SCENE':
                if len(actors):
                    ret_val[act_num][scene_num] = actors
                    actors = []
                scene_num += 1
    if len(actors):
        ret_val[act_num][scene_num] = actors
        actors = []
    return ret_val

if __name__ == '__main__':
#     import pprint
#     print get_scenes()
#     pprint.pprint(get_acts_scenes_actors())
#     p = get_play()
#     print p

    s = Scene(1)
    s.add_actor('a')
    s.add_actor('b')
    s.add_actor('c')
    s.add_actor('d')
    g = s.gen_actors()
    g
    print next(g)
    print next(g)
    print next(g)
    print next(g)
    print next(g)
#     print next(s)
#     print next(s)
#     print next(s)
#     print next(s)
#     print next(s)
    