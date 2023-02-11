import pygame
from components.component import Component

class Sprite(Component):
    """
    Simple base class for visible game objects.

    This class is responsible for rendering and updating all 
    engine graphics. It renders a single sprite per instance, 
    for an animated image check AnimateSprite()

    Derived classes can override the Sprite.update() and Sprite.draw() 
    and assign Sprite.image and Sprite.rect attributes. 

    When subclassing the Sprite class, be sure to call the base initializer.

    Attributes:
        image: surface to render
        rect: an image rectangle 
        engine: a reference to the engine object.
        screen: a reference to the display surface.
    """
    def __init__(self, actor):
        super().__init__(actor)

        self.rect = None
        self.image = None
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
