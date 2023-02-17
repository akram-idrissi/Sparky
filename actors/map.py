from .actor import Actor

class Map(Actor):
    def __init__(self, actor):
        super().__init__(actor)

    def add_layer(self, name, layer):
        self.engine.add_layer(name, layer)

    def add_animated_layer(self):
        pass

    def process_input(self, events):
        pass

    def update_actor(self):
        pass