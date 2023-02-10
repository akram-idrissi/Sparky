import pygame
from components.component import Component

class Sprite(Component):
    def __init__(self, actor):
        super().__init__(actor)

        self.rect = None
        self.image = None
        self.actor = actor
        self.engine.add_sprite(self)
        self.screen = self.window.get_screen()

    def load_img(self, img):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=self.actor.get_position())
        return self.image

    def update(self):
        self.rect.topleft = self.actor.get_position()

    def draw(self):
        self.screen.blit(self.image, (self.actor.get_position()))

    # getters setters
    def get_rect(self):
        return self.rect

    def set_rect(self, x, y):
        self.rect.topleft = (x, y)
