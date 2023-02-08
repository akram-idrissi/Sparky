import pygame
from sys import exit


class Window:
    def __init__(self):
        pygame.init()
        self.icon = ''
        self.caption = ''
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 400))

    def set_caption(self, caption):
        self.caption = caption
    
    def set_icon(self, icon):
        self.icon = icon

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def fill(self):
        self.screen.fill((0, 255, 0))   

    def close():
        pygame.quit()
        exit()
