import pygame

from window import Window
from gameObjects import load

class Game:
    def __init__(self):
        load()
        self.actors = []
        self.running = True
        self.window = Window()

        self.actors = set()

    def process_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        for actor in self.actors:
            actor.process_input(events)

    def update(self):
        for actor in self.actors:
            actor.update()

    def draw(self):
        self.window.fill()
        for actor in self.actors:
            actor.draw()
        self.window.update()

    def add_actor(self, actor):
        self.actors.add(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor) if len(self.actors) > 0  else ''

    # setters getters
    def is_running(self):
        return self.running

    def set_running(self, value):
        self.running = value
