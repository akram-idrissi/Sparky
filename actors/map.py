import csv

from .actor import Actor

class Map(Actor):
    def __init__(self, actor):
        super().__init__(actor)

        self.layers = {}

    def add_layer(self, name, layer):
        if name not in self.layers.keys() : self.layers[name] = layer

    def add_animated_layer(self):
        pass

    def process_input(self, events):
        pass

    def update_actor(self):
        pass