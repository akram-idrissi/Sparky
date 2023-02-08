import pygame

from window import Window
from gameObjects import load

class Game:
    def __init__(self):
        load()
        self.actors = []
        self.running = True
        self.window = Window()

    def processInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        for actor in self.actors:
            actor.processInput(events)

    def update(self):
        for actor in self.actors:
            actor.update()

    def draw(self):
        self.window.fill()
        for actor in self.actors:
            actor.draw()
        self.window.update()
        
    def isRunning(self):
        return self.running

    def setRunning(self, value):
        self.running = value
