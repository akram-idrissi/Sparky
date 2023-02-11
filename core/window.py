import pygame

from sys import exit
from .settings import FPS, SCREEN_COLOR, WIDTH, HEIGHT

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
        self.screen.fill(SCREEN_COLOR)   

    def close(self):
        pygame.quit()
        exit()

    # getters setters
    def get_screen(self):
        return self.screen
        