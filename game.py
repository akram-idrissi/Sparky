import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 400))
        self.window_size = pygame.display.get_window_size()
        
        self.icon = ''
        self.caption = ''

        self.actors = []

    def processInput(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
    