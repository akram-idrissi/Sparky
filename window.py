import pygame

from sys import exit
from settings import *

class Window:
    def __init__(self):
        pygame.init()
        self.icon = ''
        self.caption = ''
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(caption)
    
    def set_icon(self, icon):
        self.icon = pygame.image.load(icon)
        pygame.display.set_icon(self.icon)

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def fill(self):
        self.screen.fill(GREEN)   

    def close():
        pygame.quit()
        exit()
