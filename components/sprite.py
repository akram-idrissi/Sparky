import pygame
from .component import Component

class Sprite(Component):
    """
    Simple base class for visible game objects.

    This class is responsible for rendering and updating all 
    engine graphics. It renders a single sprite per instance, 
    for an animated image check AnimSprite()

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
        self.offset = (0, 0)
        self.engine.add_sprite(self)
        self.screen = self.window.get_screen()

    def load_img(self, img):
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=self.actor.get_position())
        return self.image

    def scale(self, x, y):
        self.image = pygame.transform.scale(self.image, (x, y))

    def update(self):
        self.rect.topleft = self.actor.get_position()

    def draw(self):
        if not self.image: return
        self.screen.blit(self.image, (self.actor.get_position()))

    def set_offset(self, n, m):
        self.offset = (n, m)

    # getters setters
    def get_rect(self):
        return self.rect

    def set_rect(self, x, y):
        self.rect.topleft = (x, y)
