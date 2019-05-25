class scene(object):
    def enter(self):
        pass

class engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        pass

class death(scene):
    def enter(self):
        pass

class laserweaponarmory(scene):
    def enter(self):
        pass

class thebridge(scene):
    def enter(self):
        pass

class the_escape_pod(scene):
    def enter(self):
        pass
    
class map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = map()
a_game = engine()
a_game.play()